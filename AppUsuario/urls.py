from django.urls import path

from . import views

urlpatterns = [
    

    path('',views.mostrar_index, name='index'),
    
    path('crear_post/', views.crear_post, name='crear'),
    path('buscador/', views.buscador, name='buscar'),
    path('mostrarpost/', views.PosteoList.as_view(), name='mostrarpost'),
    path('PosteoDetail/<pk>', views.PosteoDetail.as_view(), name='Detail'),
    path('base/', views.base, name='base'),
    path('post_confirm_delete/<pk>', views.PosteoDeleteView.as_view(), name='Eliminar'),
    path('modificar_post/<pk>', views.PosteoUpdateView.as_view(), name='Actualizar'),
    path('signup/', views.SignUpView.as_view(), name='Sign Up'),
    path('Login/', views.AdminLoginView.as_view(), name='Login'),
    path('Logout/', views.AdminLogoutView.as_view(), name='Logout'),
    path('editar_usuario/', views.editar_usuario, name='Editar usuario'),
    path('about/', views.about, name='about'),
    path('account_detail/', views.Cuenta_Detail, name='account_detail'),

]
