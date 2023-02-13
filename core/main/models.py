from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField('Menu name', max_length=50)
    name1 = models.CharField('Menu name1', max_length=50)
    name2 = models.CharField('Menu name2', max_length=50)
    name3 = models.CharField('Menu name3', max_length=50)
    name4 = models.CharField('Menu name4', max_length=50)
    img = models.ImageField('Menu image', upload_to='media', null=True)
    img1 = models.ImageField('Menu image1', upload_to='media', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menues'



class HomeHead(models.Model):
    name = models.CharField('HomeHead name', max_length=50)
    name1 = models.CharField('HomeHead name1', max_length=50)
    name2 = models.CharField('HomeHead name2', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeHead'
        verbose_name_plural = 'HomeHeads'



class Popular(models.Model):
    name = models.CharField('Popular name', max_length=50)
    name1 = models.CharField('Popular name1', max_length=50, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Popular'
        verbose_name_plural = 'Popular'



class PopularImage(models.Model):
    name = models.CharField('PopularImage name', max_length=50)
    name1 = models.CharField('PopularImage name1', max_length=50)
    about = models.TextField('PopularImage about')
    about1 = models.TextField('PopularImage about1')
    img = models.ImageField('PopularImage image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'PopularImage'
        verbose_name_plural = 'PopularImages'



class PopularEnd(models.Model):
    about = models.TextField('PopularEnd about')

    def __str__(self):
        return self.about

    class Meta:
        verbose_name = 'PopularEnd'
        verbose_name_plural = 'PopularEnds'



class Library(models.Model):
    name = models.CharField('Library name', max_length=50)
    name1 = models.CharField('Library name1', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'



class LibraryInfo(models.Model):
    name = models.CharField('LibraryInfo name', max_length=50)
    name1 = models.CharField('LibraryInfo name1', max_length=50)
    name2 = models.CharField('LibraryInfo name2', max_length=50)
    name3 = models.CharField('LibraryInfo name3', max_length=50)
    name4 = models.CharField('LibraryInfo name4', max_length=50)
    about = models.TextField('LibraryInfo about')
    about1 = models.TextField('LibraryInfo about1')
    about2 = models.TextField('LibraryInfo about2')
    about3 = models.TextField('LibraryInfo about3')
    img = models.ImageField('LibraryInfo imge', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'LibraryInfo'
        verbose_name_plural = 'LibraryInfos'



class LibraryFoot(models.Model):
    name = models.CharField('LibraryFoot name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'LibraryFoot'
        verbose_name_plural = 'LibraryFoots'



class BrowseMenu(models.Model):
    name = models.CharField('BrowseMenu name', max_length=50)
    name1 = models.CharField('BrowseMenu name1', max_length=50)
    name2 = models.CharField('BrowseMenu name2', max_length=50)
    name3 = models.CharField('BrowseMenu name3', max_length=50)
    name4 = models.CharField('BrowseMenu name4', max_length=50)
    img = models.ImageField('BrowseMenu image', upload_to='media')
    img1 = models.ImageField('BrowseMenu image1', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'BrowseMenu'
        verbose_name_plural = 'BrowseMenues'



class CaruselHead(models.Model):
    name = models.CharField('CaruselHead name', max_length=50)
    name1 = models.CharField('CaruselHead name1', max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'CaruselHead'
        verbose_name_plural = 'CaruselHeads'



class Carusel(models.Model):
    name = models.CharField('Carusel name', max_length=50)
    name1 = models.CharField('Carusel name1', max_length=50)
    about = models.TextField('Carusel about')
    about1 = models.TextField('Carusel about1')
    about2 = models.TextField('Carusel about2')
    img = models.ImageField('Carusel image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Carusel'
        verbose_name_plural = 'Carusels'



class TopHead(models.Model):
    name = models.CharField('TopHead name', max_length=50)
    name1 = models.CharField('TopHead name1', max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TopHead'
        verbose_name_plural = 'TopHeads'



class Top(models.Model):
    name = models.CharField('Top name', max_length=50)
    name1 = models.CharField('Top name1', max_length=50)
    about = models.TextField('Top about')
    about1 = models.TextField('Top about1')
    img = models.ImageField('Top image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Top'
        verbose_name_plural = 'Tops'



class TopFoot(models.Model):
    name = models.CharField('TopFoot name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TopFoot'
        verbose_name_plural = 'TopFoots'



class LiveStreamHead(models.Model):
    name = models.CharField('LiveStreamHead name', max_length=50)
    name1 = models.CharField('LiveStreamHead name1', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'LiveStreamHead'
        verbose_name_plural = 'LiveStreamHeads'



class LiveStreamBody(models.Model):
    name = models.CharField('LiveStreamBody name', max_length=50)
    about = models.TextField('LiveStreamBody about')
    img = models.ImageField('LiveStreamBody image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'LiveStreamBody'
        verbose_name_plural = 'LiveStreamBodies'



class LiveStreamFoot(models.Model):
    name = models.CharField('LiveStreamFoot name', max_length=50)
    name1 = models.CharField('LiveStreamFoot name1', max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'LiveStreamFoot'
        verbose_name_plural = 'LiveStreamFoots'



class BrowseFootHead(models.Model):
    name = models.CharField('BrowseFootHead name', max_length=50)
    name1 = models.CharField('BrowseFootHead name1', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'BrowseFootHead'
        verbose_name_plural = 'BrowseFootHeads'



class BrowseFootFoto(models.Model):
    name = models.CharField('BrowseFootFoto name', max_length=50)
    about = models.TextField('BrowseFootFoto about')
    about1 = models.TextField('BrowseFootFoto about1')
    about2 = models.TextField('BrowseFootFoto about2')
    about3 = models.TextField('BrowseFootFoto about3')
    img = models.ImageField('BrowseFootFoto image', upload_to='media')
    img1 = models.ImageField('BrowseFootFoto image1', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'BrowseFootFoto'
        verbose_name_plural = 'BrowseFootFotos'



class BrowseFootFoot(models.Model):
    name = models.CharField('BrowseFootFoot name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'BrowseFootFoot'
        verbose_name_plural = 'BrowseFootFoots'



class DetailMenu(models.Model):
    name = models.CharField('DetailMenu name', max_length=50)
    name1 = models.CharField('DetailMenu name1', max_length=50)
    name2 = models.CharField('DetailMenu name2', max_length=50)
    name3 = models.CharField('DetailMenu name3', max_length=50)
    name4 = models.CharField('DetailMenu name4', max_length=50)
    img = models.ImageField('DetailMenu image', upload_to='media')
    img1 = models.ImageField('DetailMenu image1', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'DetailMenu'
        verbose_name_plural = 'DetailMenues'



class DetailHead(models.Model):
    img = models.ImageField('DetailHead image', upload_to='media')
    img1 = models.ImageField('DetailHead image1', upload_to='media')

    def __str__(self):
        return str(self.img)

    class Meta:
        verbose_name = 'DetailHead'
        verbose_name_plural = 'DetailHeads'



class Detail(models.Model):
    name = models.CharField('Detail name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Detail'
        verbose_name_plural = 'Details'



class Sandbox(models.Model):
    name = models.CharField('Sandbox name', max_length=50)
    name1 = models.CharField('Sandbox name1', max_length=50)
    about = models.TextField('sandbox about', null=True)
    about1 = models.TextField('sandbox about1', null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sandbox'
        verbose_name_plural = 'Sandboxes'


class Action(models.Model):
    about = models.TextField('Action about')
    about1 = models.TextField('Action about1')
    about2 = models.TextField('Action about2')
    about3 = models.TextField('Action about3')

    def __str__(self):
        return self.about

    class Meta:
        verbose_name = 'Action'
        verbose_name_plural = 'Actions'



class DetailFoto(models.Model):
    img = models.ImageField('DetailFoto image', upload_to='media')

    def __str__(self):
        return str(self.img)

    class meta:
        verbose_name = 'DetailFoto'
        verbose_name_plural = 'DetailFotos'



class DetailAbout(models.Model):
    about = models.TextField('DetailAbout about')

    def __str__(self):
        return self.about

    class Meta:
        verbose_name = 'DetailAbout'
        verbose_name_plural = 'DetailAbout'



class DetailFoot(models.Model):
    name = models.CharField('DetailFoot name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'DetailFoot'
        verbose_name_plural = 'DetailFoots'



class RelatedHead(models.Model):
    name = models.CharField('RelatedHead name', max_length=50)
    name1 = models.CharField('RelatedHead name1', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'RelatedHead'
        verbose_name_plural = 'RelatedHeads'



class RelatedInfo(models.Model):
    name = models.CharField('RelatedInfo name', max_length=50)
    name1 = models.CharField('RelatedInfo name1', max_length=50)
    about = models.TextField('RelatedInfo about', null=True)
    about1 = models.TextField('RelatedInfo about1', null=True)
    img = models.ImageField('RelatedInfo image', upload_to='max')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'RelatedInfo'
        verbose_name_plural = 'RelatedInfos'



class StreamsMenu(models.Model):
    name = models.CharField('StreamsMenu name', max_length=50)
    name1 = models.CharField('StreamsMenu name1', max_length=50)
    name2 = models.CharField('StreamsMenu name2', max_length=50)
    name3 = models.CharField('StreamsMenu name3', max_length=50)
    name4 = models.CharField('StreamsMenu name4', max_length=50)
    img = models.ImageField('StreamsMenu image', upload_to='media')
    img1 = models.ImageField('StreamsMenu image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'StreamsMenu'
        verbose_name_plural = 'StreamsMenues'



class StreamsHead(models.Model):
    name = models.CharField('StreamsHead name', max_length=50)
    name1 = models.CharField('StreamsHead name1', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'StreamsHead'
        verbose_name_plural = 'StreamsHeads'



class StreamsCarusel(models.Model):
    name = models.CharField('StreamsCarusel name', max_length=50)
    name1 = models.CharField('StreamsCarusel name1', max_length=50)
    name2 = models.CharField('StreamsCarusel name2', max_length=50)
    about = models.TextField('StreamsCarusel about')
    about1 = models.TextField('StreamsCarusel about1')
    img = models.ImageField('StreamsCarusel image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'StreamsCarusel'
        verbose_name_plural = 'StreamsCarusels'



class StreamsTop(models.Model):
    name = models.CharField('StreamsTop name', max_length=50)
    name1 = models.CharField('StreamsTop name1', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'StreamsTop'
        verbose_name_plural = 'StreamsTops'



class TopInfo(models.Model):
    name = models.CharField('TopInfo name', max_length=50)
    about = models.TextField('TopInfo about')
    number = models.IntegerField('TopInfo number')
    img = models.ImageField('TopInfo image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TopInfo'
        verbose_name_plural = 'TopInfos'



class PopularHead(models.Model):
    name = models.CharField('PopularHead name', max_length=50)
    name1 = models.CharField('PopularHead name1', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'PopularHead'
        verbose_name_plural = 'PopularHeads'



class PopularFoto(models.Model):
    name = models.CharField('PopularFoto name', max_length=50)
    name1 = models.CharField('PopularFoto name1', max_length=50)
    name2 = models.CharField('PopularFoto name2', max_length=50)
    about = models.TextField('PopularFoto about')
    about1 = models.TextField('PopularFoto about1')
    img = models.ImageField('PopularFoto image',upload_to='media')
    img1 = models.ImageField('PopularFoto image1', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'PopularFoto'
        verbose_name_plural = 'PopularFotos'



class PopularFoot(models.Model):
    name = models.CharField('PopularFoot name', max_length=50)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'PopularFoot'
        verbose_name_plural = 'PopularFoots'



class ProfilMenu(models.Model):
    name = models.CharField('ProfilMenu name', max_length=50)
    name1 = models.CharField('ProfilMenu name1', max_length=50)
    name2 = models.CharField('ProfilMenu name2', max_length=50)
    name3 = models.CharField('ProfilMenu name3', max_length=50)
    name4 = models.CharField('ProfilMenu name4', max_length=50)
    img = models.ImageField('ProfilMenu image', upload_to='media')
    img1 = models.ImageField('ProfilMenu image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ProfilMenu'
        verbose_name_plural = 'ProfilMenues'



class ProfilHead(models.Model):
    name = models.CharField('ProfilHead name', max_length=50)
    name1 = models.CharField('ProfilHead name1', max_length=50)
    name2 = models.CharField('ProfilHead name2', max_length=50)
    about = models.TextField('ProfilHead about')
    about1 = models.TextField('ProfilHead about1')
    about2 = models.TextField('ProfilHead about2')
    about3 = models.TextField('ProfilHead about3')
    about4 = models.TextField('ProfilHead about4')
    about5 = models.TextField('ProfilHead about5')
    about6 = models.TextField('ProfilHead about6')
    about7 = models.TextField('ProfilHead about7')
    about8 = models.TextField('ProfilHead about8')
    img = models.ImageField('ProfilHead image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ProfilHead'
        verbose_name_plural = 'ProfilHeads'



class ProfilClip(models.Model):
    name = models.CharField('ProfilClip name', max_length=50)
    name1 = models.CharField('ProfilClip name1', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ProfilClip'
        verbose_name_plural = 'ProfilClips'



class Clip(models.Model):
    name = models.CharField('Clip name', max_length=50)
    about = models.TextField('Clip about')
    img = models.ImageField('Clip image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Clip'
        verbose_name_plural = 'Clips'



class ClipFoot(models.Model):
    name = models.CharField('ClipFoot name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ClipFoot'
        verbose_name_plural = 'ClipFoots'



class ProfilLibrary(models.Model):
    name = models.CharField('ProfilLibrary name', max_length=50)
    name1 = models.CharField('ProfilLibrary name1', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ProfilLibrary'
        verbose_name_plural = 'ProfilLibraries'



class ProfilLibraryFoto(models.Model):
    name = models.CharField('ProfilLibraryFoto name', max_length=50)
    name1 = models.CharField('ProfilLibraryFoto name1', max_length=50)
    name2 = models.CharField('ProfilLibraryFoto name2', max_length=50)
    name3 = models.CharField('ProfilLibraryFoto name3', max_length=50)
    name4 = models.CharField('ProfilLibraryFoto name4', max_length=50)
    about = models.TextField('ProfilLibraryFoto about')
    about1 = models.TextField('ProfilLibraryFoto about1')
    about2 = models.TextField('ProfilLibraryFoto about2')
    about3 = models.TextField('ProfilLibraryFoto about3')
    img = models.ImageField('ProfilLibraryFoto image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ProfilLibraryFoto'
        verbose_name_plural = 'ProfilLibraryFotos'








