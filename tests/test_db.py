import unittest
from peewee import *
from app import TimelinePost


MODELS = [TimelinePost]
test_db = SqliteDatabase(":memory:")


class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        #Create two timeline post & check if info is correct
        first_post = TimelinePost.create(
            name="Omar Macias",
            email="omarmacias@example.com",
            content="Creating tests"
        )
        self.assertEqual(first_post.id, 1)
        second_post = TimelinePost.create(
            name="Juan Perez",
            email="juanperez@example.com",
            content="Making tests"
        )
        self.assertEqual(second_post.id, 2)

        posts = TimelinePost.select()
        self.assertEqual(posts.count(), 2)
        
        self.assertEqual(posts[0].name, "Omar Macias")
        self.assertEqual(posts[1].name, "Juan Perez")
        
        self.assertEqual(posts[0].email, "omarmacias@example.com")
        self.assertEqual(posts[1].email, "juanperez@example.com")
        
        self.assertEqual(posts[0].content, "Creating tests")
        self.assertEqual(posts[1].content, "Making tests")
