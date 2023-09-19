from django.urls import path
from main.views import main_view, add_item, xml_format, xml_format_by_id, json_format, json_format_by_id

app_name = "main"

urlpatterns = [
    path("main/", main_view, name="main_view"),
    path("add_item/", add_item, name="add_item"),
    path("xml/", xml_format, name="xml_format"),
    path("json/", json_format, name="json_format"),
    path("json/<int:id>", json_format_by_id, name="json_format_by_id"),
    path("xml/<int:id>", xml_format_by_id, name="xml_format_by_id"),
]