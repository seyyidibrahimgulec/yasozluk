# from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from interactions.forms import NewMessageForm
from interactions.models import Message
from django.urls import reverse
from django.contrib.auth.models import User


def messages(request, user_id=-1, slug=""):
    print("user_id", user_id, "currentuser", request.user.id)
    if user_id == request.user.id:
        return redirect(reverse("allMessages"))
    current_user = {}
    current_conversation = {}
    if user_id != -1:
        current_conversation = Message.objects.filter(
            (Q(send_by_id=request.user.id) & Q(send_to_id=user_id)) |
            (Q(send_to_id=request.user.id) & Q(send_by_id=user_id))).order_by("-created_at")
        current_user = User.objects.get(pk=user_id)

    incoming = Message.objects.filter(
        send_to__id=request.user.id).values('send_by__id').distinct()
    outbox = Message.objects.filter(
        send_by__id=request.user.id).values('send_to__id').distinct()

    # page = request.GET.get('page', 1)
    #
    # paginator = Paginator(all_messages, 10)  # Show 25 contacts per page.
    # try:
    #     paged_ids = paginator.page(page)
    # except PageNotAnInteger:
    #     # fallback to the first page
    #     paged_ids = paginator.page(1)
    # except EmptyPage:
    #     # probably the user tried to add a page number
    #     # in the url, so we fallback to the last page
    #     paged_ids = paginator.page(paginator.num_pages)

    paged_messages = []
    for item in incoming:
        print(item['send_by__id'])
        last_message = Message.objects. \
            filter((Q(send_by_id=request.user.id) & Q(send_to_id=item['send_by__id'])) |
                   (Q(send_to_id=request.user.id) & Q(send_by_id=item['send_by__id']))). \
            order_by("-created_at").first()
        if not last_message:
            continue

        sender = last_message.send_by
        if sender.id == request.user.id:
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
            filter((Q(send_by_id=request.user.id) & Q(send_to_id=item['send_to__id'])) |
                   (Q(send_to_id=request.user.id) & Q(send_by_id=item['send_to__id']))). \
            order_by("-created_at").first()
        if not last_message:
            continue
        sender = last_message.send_by
        if sender.id == request.user.id:
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

    return render(request,
                  'userMessages.html',
                  {'messages': paged_messages,
                   'me': request.user.id,
                   'conversationWith': current_user,
                   'current_conversation': current_conversation})


def message_item_sort_key(val):
    return val['date']


def newMessage(request):
    # allMessages = Message.objects.filter(send_to__pk=request.user.id)
    allMessages = Message.objects.filter(Q(send_to__id=request.user.id) |
                                         Q(send_by__id=request.user.id))
    # targetUser = User.objects.filter(pk=num)

    if request.method == 'POST':
        form = NewMessageForm(request.POST, user=request.user)
        if form.is_valid():
            new_saved = form.save()
            print("saved with:", new_saved.pk)
            redir_user = new_saved.send_by
            if redir_user.pk == request.user.id:
                redir_user = new_saved.send_to
            return redirect(reverse(messages,
                                    kwargs={'user_id': redir_user.id,
                                            'slug': redir_user.username}))
    else:
        form = NewMessageForm(user=request.user)
    return render(request, 'newMessage.html',
                  {'form': form, 'allMessages': allMessages})


def newMessageAjax(request):
    print("calling ajax?")
