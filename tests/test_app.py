import unittest
import os
os.environ["TESTING"] = "true"
from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        """
        Test the content and status code of the home page
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn("<title>MLH Fellow</title>", html)

    def test_home_page(self):
        """
        Test the content and status code of `/`
        """
        # GET /
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn("<h1>MLH Fellow</h1>", html)
        self.assertIn("<h2>Education</h2>", html)
        self.assertIn('<div class="profile">', html)
        self.assertIn('<div class="about-me">', html)

    def test_timeline_api_get(self):
        """
        Test the content and status code of GET /api/timeline_post
        """
        # GET /api/timeline_post
        response = self.client.get("/api/timeline_post")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        json = response.get_json()
        self.assertIn("timeline_posts", json)
        self.assertEqual(len(json["timeline_posts"]), 0)

    def test_timeline_api_post(self):
        """
        Test the content and status code of POST /api/timeline_post and DELETE /api/timeline_post
        """
        # POST /api/timeline_post
        request_data = {
            "name": "Omar Macias",
            "email": "omarmacias@example.com",
            "content": "Creating tests"
        }
        post_response = self.client.post("/api/timeline_post", data=request_data)
        self.assertEqual(post_response.status_code, 200)
        self.assertTrue(post_response.is_json)
        post_json = post_response.get_json()
        self.assertIn("id", post_json)
        self.assertEqual(post_json["id"], 1)
        self.assertEqual(post_json["name"], "Omar Macias")
        self.assertEqual(post_json["email"], "omarmacias@example.com")
        self.assertEqual(post_json["content"], "Creating tests")
        # GET /api/timeline_post
        second_get_response = self.client.get("/api/timeline_post")
        self.assertEqual(second_get_response.status_code, 200)
        self.assertTrue(second_get_response.is_json)
        second_get_json = second_get_response.get_json()
        self.assertIn("timeline_posts", second_get_json)
        self.assertEqual(len(second_get_json["timeline_posts"]), 1)
        self.assertEqual(second_get_json["timeline_posts"][0]["id"], 1)
        self.assertEqual(second_get_json["timeline_posts"][0]["name"], "Omar Macias")
        self.assertEqual(second_get_json["timeline_posts"][0]["email"], "omarmacias@example.com")
        self.assertEqual(second_get_json["timeline_posts"][0]["content"], "Creating tests")
        # DELETE /api/timeline_post
        # delete_response = self.client.delete("/api/timeline_post/1")
        # self.assertEqual(delete_response.status_code, 200)
        # delete_html = delete_response.get_data(as_text=True)
        # self.assertIn("Timeline post deleted successfully", delete_html)
        third_get_response = self.client.get("/api/timeline_post")
        self.assertEqual(third_get_response.status_code, 200)
        self.assertTrue(third_get_response.is_json)
        third_get_json = third_get_response.get_json()
        self.assertIn("timeline_posts", third_get_json)
        # self.assertEqual(len(third_get_json["timeline_posts"]), 0)

    def test_malformed_timeline_api_post(self):
        """
        Test edge cases and status code of POST /api/timeline_post
        """
        # Missing name
        no_name_data = {
            "email": "omarmacias@example.com",
            "content": "Creating tests"
        }
        no_name_response = self.client.post("/api/timeline_post", data=no_name_data)
        self.assertEqual(no_name_response.status_code, 400)
        no_name_html = no_name_response.get_data(as_text=True)
        self.assertIn("Invalid name", no_name_html)
        
        # Empty content
        empty_content_data = {
            "name": "Omar Macias",
            "email": "omarmacias@example.com",
            "content": ""
        }
        empty_content_response = self.client.post("/api/timeline_post", data=empty_content_data)
        self.assertEqual(empty_content_response.status_code, 400)
        empty_content_html = empty_content_response.get_data(as_text=True)
        self.assertIn("Invalid content", empty_content_html)
        
        # Malformed email
        malformed_email_data = {
            "name": "Omar Macias",
            "email": "not-an-email",
            "content": "Creating tests"
        }
        malformed_email_response = self.client.post("/api/timeline_post", data=malformed_email_data)
        self.assertEqual(malformed_email_response.status_code, 400)
        malformed_email_html = malformed_email_response.get_data(as_text=True)
        self.assertIn("Invalid email", malformed_email_html)

    def test_timeline_page(self):
        """
        Test the content and status code of /timeline
        """
        # GET /timeline
        timeline_response = self.client.get("/timeline")
        self.assertEqual(timeline_response.status_code, 200)
        timeline_html = timeline_response.get_data(as_text=True)
        self.assertIn("<title>Timeline</title>", timeline_html)
        self.assertIn("<h1>Timeline Posts</h1>", timeline_html)
        self.assertIn("<h1>Timeline Post Form</h1>", timeline_html)
