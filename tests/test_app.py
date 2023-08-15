import unittest
import os
os.environ["TESTING"] = "true"
from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn("<title>Gabriela Liera</title>", html)
        self.assertIn("Welcome to my website", html)
    
    def test_timeline_page(self):
        # GET /timeline -content & status code
        timeline_response = self.client.get("/timeline")
        self.assertEqual(timeline_response.status_code, 200)
        timeline_html = timeline_response.get_data(as_text=True)
        self.assertIn("<title>Timeline</title>", timeline_html)
        self.assertIn("Timeline", timeline_html)
        self.assertIn("Recent Posts", timeline_html)

    def test_timeline_api_get(self):
        # GET /api/timeline_post
        response = self.client.get("/api/timeline_post")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        json = response.get_json()
        self.assertIn("timeline_posts", json)
        self.assertEqual(len(json["timeline_posts"]), 0)

    def test_timeline_api_post(self):        
        test_data = {
            'name': "John Test",
            'email': "john@testing.com",
            'content': "Testing timeline post API"
        }
        response = self.client.post("/api/timeline_post", data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        postJSON = response.get_json()
        
        self.assertIn("id", postJSON)
        self.assertEqual(postJSON["name"], test_data["name"])
        self.assertEqual(postJSON["email"], test_data["email"])
        self.assertEqual(postJSON["content"], test_data["content"])
    
    def test_timeline_api_post_then_get(self):
        post_data = {
            "name": "Omar Macias",
            "email": "omarmacias@example.com",
            "content": "Testing timeline API post -> get"
        }
        postResponse = self.client.post("/api/timeline_post", data=post_data)
        self.assertEqual(postResponse.status_code, 200)
        
        getResponse = self.client.get("/api/timeline_post")
        self.assertEqual(getResponse.status_code, 200)
        
        self.assertTrue(getResponse.is_json)
        getJSON = getResponse.get_json()
       
        self.assertIn("timeline_posts", getJSON)
        self.assertGreater(len(getJSON['timeline_posts']), 0)
        self.assertEqual(getJSON["timeline_posts"][0]["name"], post_data["name"])
        self.assertEqual(getJSON["timeline_posts"][0]["email"], post_data["email"])
        self.assertEqual(getJSON["timeline_posts"][0]["content"], post_data["content"])

    def test_timeline_api_post_then_delete(self):
        post_data = {
            "name": "Omar Macias",
            "email": "omarmacias@example.com",
            "content": "Testing timeline API post -> delete"
        }
        
        postResponse = self.client.post("/api/timeline_post", data=post_data)
        self.assertEqual(postResponse.status_code, 200)
        self.assertTrue(postResponse.is_json)
        postJSON = postResponse.get_json()
        postID = postJSON["id"]

        #GET to ensure data deleted afterwards
        first_get_respsonse = self.client.get("/api/timeline_post")
        self.assertEqual(first_get_respsonse.status_code, 200)
        self.assertTrue(first_get_respsonse.is_json)
        first_get_json = first_get_respsonse.get_json()

        #Delete post
        deleteResponse = self.client.delete("/api/timeline_post", data={"id": postID})
        self.assertEqual(deleteResponse.status_code, 200)
        self.assertTrue(deleteResponse.is_json)
        deleteJSON = deleteResponse.get_json()

        self.assertEqual(deleteJSON["name"], post_data["name"])
        self.assertEqual(deleteJSON["email"], post_data["email"])
        self.assertEqual(deleteJSON["content"], post_data["content"])

        
        #2nd GET to ensure data deleted
        second_get_respsonse = self.client.get("/api/timeline_post")
        self.assertEqual(second_get_respsonse.status_code, 200)
        self.assertTrue(second_get_respsonse.is_json)
        second_get_json = second_get_respsonse.get_json()

        self.assertLess(len(second_get_json["timeline_posts"]), len(first_get_json["timeline_posts"]))
       

    def test_malformed_timeline_api_post(self):
        """
        Test edge cases and status code of POST /api/timeline_post
        """
        # POST: Missing name
        no_name_data = {
            "email": "omarmacias@example.com",
            "content": "Creating tests"
        }
        no_name_response = self.client.post("/api/timeline_post", data=no_name_data)
        self.assertEqual(no_name_response.status_code, 400)
        no_name_html = no_name_response.get_data(as_text=True)
        self.assertIn("Invalid name", no_name_html)
        
        #POST: Malformed email
        malformed_email_data = {
            "name": "Omar Macias",
            "email": "not-an-email",
            "content": "Creating tests"
        }
        malformed_email_response = self.client.post("/api/timeline_post", data=malformed_email_data)
        self.assertEqual(malformed_email_response.status_code, 400)
        malformed_email_html = malformed_email_response.get_data(as_text=True)
        self.assertIn("Invalid email", malformed_email_html)

         #POST: Empty content
        empty_content_data = {
            "name": "Omar Macias",
            "email": "omarmacias@example.com",
            "content": ""
        }
        empty_content_response = self.client.post("/api/timeline_post", data=empty_content_data)
        self.assertEqual(empty_content_response.status_code, 400)
        empty_content_html = empty_content_response.get_data(as_text=True)
        self.assertIn("Invalid content", empty_content_html)
    
