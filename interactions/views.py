# from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.timezone import make_aware
from django.views.generic import ListView, CreateView

from interactions.forms import NewMessageForm
from interactions.models import Message


@method_decorator(login_required, name="dispatch")
class MessagesView(ListView):
    context_object_name = "messages"
    template_name = "userMessages.html"

    def get_user_messages(self):
        incoming = Message.objects.filter(
            send_to__id=self.request.user.id).values('send_by__id').distinct()
        outbox = Message.objects.filter(
            send_by__id=self.request.user.id).values('send_to__id').distinct()
        paged_messages = []
        for item in incoming:
            print(item['send_by__id'])
            last_message = Message.objects. \
                filter((Q(send_by_id=self.request.user.id) & Q(send_to_id=item['send_by__id'])) |
                       (Q(send_to_id=self.request.user.id) & Q(send_by_id=item['send_by__id']))). \
                order_by("-created_at").first()
            if not last_message:
                continue

            sender = last_message.send_by
            if sender.id == self.request.user.id:
                sender = last_message.send_to

            paged_messages.append({
                'user_id': sender.id,
                'target': sender.username,
                'text': last_message.text[:25],
                'date': last_message.created_at
            })
        for item in outbox:
            print(item['send_to__id'])
            last_message = Message.objects. \
                filter((Q(send_by_id=self.request.user.id) & Q(send_to_id=item['send_to__id'])) |
                       (Q(send_to_id=self.request.user.id) & Q(send_by_id=item['send_to__id']))). \
                order_by("-created_at").first()
            if not last_message:
                continue
            sender = last_message.send_by
            if sender.id == self.request.user.id:
                sender = last_message.send_to

            message_item = {
                'user_id': sender.id,
                'target': sender.username,
                'text': last_message.text[:25],
                'date': last_message.created_at
            }
            if message_item in paged_messages:
                print("already added")
                continue

            paged_messages.append(message_item)

        paged_messages.sort(key=message_item_sort_key, reverse=True)
        return paged_messages

    def get_context_data(self, *, object_list=None, **kwargs):
        user_id = -1
        kwargs['conversationWith'] = {}
        kwargs['current_conversation'] = {}

        if "user_id" in self.kwargs:
            user_id = self.kwargs["user_id"]

        if user_id != -1:
            kwargs['current_conversation'] = Message.objects.filter(
                (Q(send_by_id=self.request.user.id) & Q(send_to_id=user_id)) |
                (Q(send_to_id=self.request.user.id) & Q(send_by_id=user_id))).order_by("created_at")
            kwargs['conversationWith'] = User.objects.get(pk=user_id)
            kwargs['me'] = self.request.user.id

        # kwargs["messages"] = self.get_user_messages()
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        if self.queryset is not None or self.model is not None:
            return super().get_queryset()
        return self.get_user_messages()


def message_item_sort_key(val):
    return val['date']


@method_decorator(login_required, name="dispatch")
class NewMessageView(MessagesView):
    template_name = "newMessage.html"

    def get_context_data(self, **kwargs):
        kwargs["form"] = NewMessageForm(user=self.request.user)
        return super().get_context_data(**kwargs)

    def post(self, request):
        form = NewMessageForm(request.POST, user=request.user)
        if form.is_valid():
            new_saved = form.save()
            print("saved with:", new_saved.pk)
            redir_user = new_saved.send_by
            if redir_user.pk == request.user.id:
                redir_user = new_saved.send_to
            return redirect(reverse_lazy('messagesRoute',
                                         kwargs={'user_id': redir_user.id,
                                                 'slug': redir_user.username}))


# login_required attribute is being added in urls.py
class NewMessageAjax:
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        form.instance.send_by = self.request.user
        form.instance.send_to = User.objects.get(pk=int(form.data["send_to_id"]))
        response = super().form_valid(form)

        if self.request.is_ajax():
            entry = self.object
            me = self.request.user.id
            return render(self.request, 'includes/message.html', locals())
        else:
            return response


class MessageCreate(NewMessageAjax, CreateView):
    model = Message
    fields = ['text']
    success_url = reverse_lazy('allMessages')


def poll_message_count(request):
    last_poll = make_aware(datetime.fromisoformat(request.GET.get("lastPoll")))
    count = Message.objects.filter(
        Q(send_to__id=request.user.id) & Q(created_at__gte=last_poll)).count()
    # print(count)
    return JsonResponse({'count': count})


def get_message_poll(request):
    last_poll = make_aware(datetime.fromisoformat(request.GET.get("lastPoll")))
    data = Message.objects.filter(
        Q(send_to__id=request.user.id) & Q(created_at__gte=last_poll)).order_by("created_at")

    current_conversation = data
    me = request.user.id
    print(data)
    return render(request, 'includes/conversation.html', locals())
