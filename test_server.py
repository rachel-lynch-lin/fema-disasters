import unittest
import server 
from model import connect_to_db, db, User
class TestServer(unittest.TestCase):
    
    def setUp(self):
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True
        server.app.config['SECRET_KEY'] = 'key'
        connect_to_db(server.app, "postgresql:///testdb")
        
        db.create_all()
        example_data()

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = User.query.first().id
    def tearDown(self):
      """Stuff to do after each test."""


    def test_index(self):
        result = self.client.get('/')
        self.assertIn(b'<li>User.query.first().id</li>', result.data)

    # def test_register_user(self):
    #     self.assertEqual('foo'.upper(), 'jOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)
def example_data():
    """Create some sample data."""

    # In case this is run more than once, empty out existing data
    # Event.query.delete()
    # Grant.query.delete()
    User.query.delete()
    # UserSearch.query.delete()

    # Add sample incidents and Events
    # df = Event(fema_id='fin', dept='Finance', phone='555-1000')
    # dl = Event(fema_id='legal', dept='Legal', phone='555-2222')
    # dm = Event(fema_id='mktg', dept='Marketing', phone='555-9999')

    dog = User(username='dog', password="bark", email="dog@dog.com")
    # liz = Employee(name='Liz', dept=dl)
    # maggie = Employee(name='Maggie', dept=dm)
    # nadine = Employee(name='Nadine')

    db.session.add_all([dog])
    db.session.commit()

if __name__ == '__main__':
    unittest.main()