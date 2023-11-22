from django.urls import path
from main.views import render_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user, increase_amount, decrease_amount, remove_item
from main.views import get_item_json, add_item_ajax, remove_item_ajax, create_item_flutter, get_user_items




app_name = 'main'

urlpatterns = [
    path('', render_main, name='render_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increase-amount/<int:item_id>/', increase_amount, name='increase_amount'),
    path('decrease-amount/<int:item_id>/', decrease_amount, name='decrease_amount'),
    path('remove-item/<int:item_id>/', remove_item, name='remove_item'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-ajax/', add_item_ajax, name='add_item_ajax'),
    path('remove-item-ajax/<int:item_id>/', remove_item_ajax, name='remove_item_ajax'),
    path('create-flutter/', create_item_flutter, name='create_item_flutter'),
    path('get-user-items/', get_user_items, name='get_user_items')
]   