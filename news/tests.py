from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt
# Create your tests here.
class EditorTestClass(TestCase):
    def setUp(self):
        self.collins=Editor(first_name="Collins",last_name="kipke",email="collins@gamil.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.collins,Editor))

    def test_save_method(self):
        self.collins.save_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)>0)

    def test_delete_method(self):
        self.collins.del_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)==0)

class TagTestClass(TestCase):
    def setUp(self):
        self.tag=tags(id=1)

    def test_tags(self):
        self.assertEqual(self.tag.id,1)

    def test_instance(self):
        self.assertTrue(isinstance(self.tag,tags))

    def test_save_method(self):
        self.tag.save_tag()
        tag=tags.objects.all()
        self.assertTrue(len(tag)>0)

    def test_delete_method(self):
        self.tag.del_tag()
        tag=tags.objects.all()
        self.assertTrue(len(tag)==0)

class ArticleTestClass(TestCase):
    def setUp(self):
        self.collins=Editor(first_name="Collins",last_name="kipke",email="collins@gamil.com")
        self.collins.save_editor()

        self.new_tag=tags(name="testing")
        self.new_tag.save()

        self.new_article=Article(title="Barcelona",post='beaten like shiet ',editor=self.collins)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)


    def tearDown(self):
        Editor.objects.all().delete()
        Article.objects.all().delete()
        tags.objects.all().delete()

    def test_get_news_today(self):
        todayNews=Article.today_news()
        self.assertTrue(len(todayNews)>0)

    def test_get_news_by_date(self):
        test_date='2010-05-08'
        date=dt.datetime.strptime(test_date,'%Y-%m-%d').date()
        news_by_date=Article.days_news(date)
        self.assertTrue(len(news_by_date)==0)
