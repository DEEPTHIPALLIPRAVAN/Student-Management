from django.urls import path
from app import views

urlpatterns = [
    path('',views.nav,name='nav'),
    path('tch',views.addteacher,name='addteacher'),
    path('lg',views.user_log,name='user_log'),
    path('streg',views.studregister,name='studregister'),
    path('st',views.sthome,name='sthome'),
    path('ad',views.adminhome,name='adminhome'),
    path('teac',views.teacherhome,name='teacherhome'),
    path('viewt',views.teacherview,name='teacherview'),
    path('delete/<int:id>',views.deleteteacher,name='deleteteacher'),
    path('edit/<int:tt>',views.editteacher,name='editteacher'),
    path('updatet/<int:tt>',views.updateteacher,name='updateteacher'),
    path('views',views.studentview,name='studentview'),
    path('sdelete/<int:id>',views.deletestudent,name='deletestudent'),
    path('sedit/<int:ss>',views.editstudent,name='editstudent'),
    path('supdate/<int:ss>',views.updatestudent,name='updatestudent'),
    path('profileedit',views.stuprofedit,name='stuprofedit'),
    path('profupdate',views.studprofupdate,name='studprofupdate'),
    path('viewtprof',views.teacherprofile,name='teacherprofile'),
    path("lgout",views.logouts,name='logouts'),
    path('stutch',views.stutchview,name='stutchview'),


]