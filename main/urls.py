from django.urls import path
from main.views import main_view, add_item, xml_format, xml_format_by_id, json_format, json_format_by_id
from main.views import register, login_user, logout_user, add_amount, delete_data, sub_amount, get_item_json, add_item_ajax
from main.views import delete_item_ajax

app_name = "main"

urlpatterns = [
    path("main/", main_view, name="main_view"),
    path("add_item/", add_item, name="add_item"),
    path("xml/", xml_format, name="xml_format"),
    path("json/", json_format, name="json_format"),
    path("json/<int:id>", json_format_by_id, name="json_format_by_id"),
    path("xml/<int:id>", xml_format_by_id, name="xml_format_by_id"),
    path('register/', register, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path("main/add_amount/<int:id>",add_amount, name="add_amount"),
    path("main/delete_data/<int:id>",delete_data, name="delete_data"),
    path("main/sub_amount/<int:id>",sub_amount, name="sub_amount"),
    path("get-item/", get_item_json, name="get_item_json"),
    path("main/create-ajax/", add_item_ajax, name="add_item_ajax"),
    path("main/delete_item_ajax/<int:id>", delete_item_ajax, name="delete_item_ajax"),
]