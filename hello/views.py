from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

users = []


def get_free_id():
    existing_ids = {u["id"] for u in users}
    i = 1
    while i in existing_ids:
        i += 1
    return i


def index(request):
    output = '<p><a href="/users/">Users</a></p>'
    output += '<p><a href="/forum/">Forum</a></p>'
    output += '<p><a href="/contact/">Contact</a></p>'
    output += '<p><a href="/arxiv/">Arxiv</a></p>'
    return HttpResponse(output)


def users_view(request):
    output = "<h2>Users</h2>"
    if users:
        for u in sorted(users, key=lambda x: x["id"]):
            output += f'<p><a href="/{u["name"]}/">{u["id"]}. {u["name"]}</a></p>'
    else:
        output += "<p>Userler joq</p>"
    return HttpResponse(output)


def user_page(request, name):
    if name in ["favicon.ico", "static"]:
        return HttpResponseNotFound()

    user = None
    for u in users:
        if u["name"].lower() == name.lower():
            user = u
            break

    if user is None:
        new_id = get_free_id()
        user = {
            "id": new_id,
            "name": name,
            "views": 1,
        }
        users.append(user)
    else:
        user["views"] += 1

    output = f"<h2>User: {user['name']}</h2>"
    output += f"<p>Nomer: {user['id']}</p>"
    output += f"<p>Ati: {user['name']}</p>"
    output += f"<p>Korilgeni (zaproslar sani): {user['views']}</p>"
    output += '<p><a href="/users/">Users</a></p>'
    output += '<p><a href="/forum/">Forum</a></p>'
    output += '<p><a href="/contact/">Contact</a></p>'
    output += '<p><a href="/arxiv/">Arxiv</a></p>'
    return HttpResponse(output)


def forum_view(request):
    output = "<h2>Forum</h2>"
    if users:
        for u in sorted(users, key=lambda x: x["id"]):
            output += f'<p>{u["id"]}. {u["name"]} <a href="/forum/delete/{u["id"]}/">oshiriw</a></p>'
    else:
        output += "<p>Userler joq</p>"
    return HttpResponse(output)


def forum_delete(request, id):
    global users
    users = [u for u in users if u["id"] != id]
    return HttpResponseRedirect("/forum/")


def contact_view(request):
    output = "<h2>Contact</h2>"
    if users:
        for u in sorted(users, key=lambda x: x["id"]):
            output += f'<p>{u["id"]}. {u["name"]} - korilgeni (zaproslar sani): {u["views"]}</p>'
    else:
        output += "<p>Userler joq</p>"
    return HttpResponse(output)


def arxiv_view(request):
    output = "<h2>Arxiv</h2>"
    if users:
        for u in sorted(users, key=lambda x: x["id"]):
            output += f'<p>{u["name"]}</p>'
    else:
        output += "<p>Userler joq</p>"
    return HttpResponse(output)
