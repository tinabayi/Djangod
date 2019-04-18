from django.test import TestCase
from .models import Image,Profile,Comment,Rating
# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.project= Editor(project = 'image', project_name ='run', project_description='Running is a method of terrestrial locomotion allowing humans and other animals to move rapidly on foot. Running is a type of gait characterized by an aerial phase in which all feet are above the ground.',comments='It dangerous',project_url='https://www.lipsum.com/')

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))



     # Testing Save Method
    def test_save_method(self):
        self.image.save_image()
        projects = Image.objects.all()
        self.assertTrue(len(projects) > 0)    