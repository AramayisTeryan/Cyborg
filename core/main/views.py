from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Menu, HomeHead, Popular, PopularImage, PopularEnd, Library, LibraryInfo, LibraryFoot, BrowseMenu, CaruselHead, Carusel, TopHead, Top, TopFoot, LiveStreamHead, LiveStreamBody, LiveStreamFoot, BrowseFootHead, BrowseFootFoto, BrowseFootFoot, DetailMenu, DetailHead, Detail, Sandbox, Action, DetailFoto, DetailAbout, DetailFoot, RelatedHead, RelatedInfo, StreamsMenu, StreamsHead, StreamsCarusel, StreamsTop, TopInfo, PopularHead, PopularFoto, PopularFoot, ProfilMenu, ProfilHead, ProfilClip, Clip, ClipFoot, ProfilLibrary, ProfilLibraryFoto

# Create your views here.

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        menu = Menu.objects.all()
        homehead = HomeHead.objects.all()
        popular = Popular.objects.all()
        popularimage = PopularImage.objects.all()
        popularend = PopularEnd.objects.all()
        library = Library.objects.all()
        libraryinfo = LibraryInfo.objects.all()
        libraryfoot = LibraryFoot.objects.all()
        return render(request, self.template_name, {'menu':menu, 'homehead':homehead, 'popular':popular, 'popularimage':popularimage, 'popularend':popularend, 'library':library, 'libraryinfo':libraryinfo, 'libraryfoot':libraryfoot})


class BrowseListView(ListView):
    template_name = 'browse.html'

    def get(self, request):
        browsemenu = BrowseMenu.objects.all()
        caruselhead = CaruselHead.objects.all()
        carusel = Carusel.objects.all()
        tophead = TopHead.objects.all()
        top = Top.objects.all()
        topfoot = TopFoot.objects.all()
        livestreamhead = LiveStreamHead.objects.all()
        livestreambody = LiveStreamBody.objects.all()
        livestreamfoot = LiveStreamFoot.objects.all()
        browsefoothead = BrowseFootHead.objects.all()
        browsefootfoto = BrowseFootFoto.objects.all()
        browsefootfoot = BrowseFootFoot.objects.all()
        return render(request, self.template_name, {'browsemenu':browsemenu, 'caruselhead':caruselhead, 'carusel':carusel, 'tophead':tophead, 'top':top, 'topfoot':topfoot, 'livestreamhead':livestreamhead, 'livestreambody':livestreambody, 'livestreamfoot':livestreamfoot, 'browsefoothead':browsefoothead, 'browsefootfoto':browsefootfoto, 'browsefootfoot':browsefootfoot})


class DetailsListView(ListView):
    template_name = 'details.html'

    def get(self, request):
        detailmenu = DetailMenu.objects.all()
        detailhead = DetailHead.objects.all()
        detail = Detail.objects.all()
        sandbox = Sandbox.objects.all()
        action = Action.objects.all()
        detailfoto = DetailFoto.objects.all()
        detailabout = DetailAbout.objects.all()
        detailfoot = DetailFoot.objects.all()
        relatedhead  = RelatedHead.objects.all()
        relatedinfo = RelatedInfo.objects.all()
        return render(request, self.template_name, {'detailmenu':detailmenu, 'detailhead':detailhead, 'detail':detail, 'sandbox':sandbox, 'action':action, 'detailfoto':detailfoto, 'detailabout':detailabout, 'detailfoot':detailfoot, 'relatedhead':relatedhead, 'relatedinfo':relatedinfo})


class StreamsListView(ListView):
    template_name = 'streams.html'

    def get(self, request):
        streamsmenu = StreamsMenu.objects.all()
        streamshead = StreamsHead.objects.all()
        streamscarusel = StreamsCarusel.objects.all()
        streamstop = StreamsTop.objects.all()
        topinfo = TopInfo.objects.all()
        popularhead = PopularHead.objects.all()
        popularfoto = PopularFoto.objects.all()
        popularfoot = PopularFoot.objects.all()
        return render(request, self.template_name, {'streamsmenu':streamsmenu, 'streamshead':streamshead, 'streamscarusel':streamscarusel, 'streamstop':streamstop, 'topinfo':topinfo, 'popularhead':popularhead, 'popularfoto':popularfoto, 'popularfoot':popularfoot})


class ProfilListView(ListView):
    template_name = 'profile.html'

    def get(self, request):
        profilmenu = ProfilMenu.objects.all()
        profilhead = ProfilHead.objects.all()
        profilclip = ProfilClip.objects.all()
        clip = Clip.objects.all()
        clipfoot = ClipFoot.objects.all()
        profillibrary = ProfilLibrary.objects.all()
        profillibraryfoto = ProfilLibraryFoto.objects.all()
        return render(request, self.template_name, {'profilmenu':profilmenu, 'profilhead':profilhead, 'profilclip':profilclip, 'clip':clip, 'clipfoot':clipfoot, 'profillibrary':profillibrary, 'profillibraryfoto':profillibraryfoto})
