import logging

from example_server.controllers.base_controller import BaseController

from swagger_server.models.example import Example
from swagger_server.models.examples import Examples


class ExampleController(BaseController):

    def create_example(self, example, user=None, auths=None):
        """
        create_example
        Create a example
        :param example: 
        :type example: dict | bytes

        :rtype: Example
        """

        ret_code = 200
        ret_value = example


        with self._connection:
           with self._connection.cursor() as cursor:
               cursor.execute('''INSERT INTO example
                              (example_value) VALUES (%s) 
                              RETURNING example_id''',
                              (example.example_value,))
               ret_value = Example(None, example_value=example.example_value)
               ret_value.example_id = cursor.fetchone()[0]
               ret_code = 201

        return ret_value, ret_code


    def download_example(self, exampleId, user=None, auths=None):
        """
        fetches an example
        
        :param exampleId: ID of example to fetch
        :type exampleId: str

        :rtype: Example
        """
        ret_code = 200
        ret_value = None

        cur = self._connection.cursor()

        with self._connection:
          with self._connection.cursor() as cursor:
            cursor.execute('SELECT example_id, example_value FROM example WHERE example_id = %s',
                       (exampleId,))

            for (eid, evalue) in cursor:
                ret_value = Example(eid, example_value=evalue)

        if not ret_value:
            ret_code = 404

        return ret_value, ret_code

    def download_examples(self, user=None, auths=None):
        """
        fetches examples
        
        :param studyName: restrict to a particular study
        :type studyName: str
        :param start: for pagination start the result set at a record x
        :type start: int
        :param count: for pagination the number of entries to return
        :type count: int
        :param orderby: how to order the result set
        :type orderby: str

        :rtype: Examples
        """
        ret_code = 200
        ret_value = Examples()

        ret_value.count = 0
        ret_value.items = []

        with self._connection:
          with self._connection.cursor() as cursor:
            cursor.execute('SELECT example_id, example_value FROM example')

            for (eid, evalue) in cursor:
                ret_value.items.append(Example(eid, example_value=evalue))
                ret_value.count = ret_value.count + 1

        return ret_value, ret_code


    def update_example(self, example, user=None, auths=None):
        """
        updates an example
        
        :param example: 
        :type example: dict | bytes

        :rtype: Example
        """

        ret_code = 200
        ret_value = None

        with self._connection:
          with self._connection.cursor() as cursor:
            cursor.execute('''UPDATE example SET example_value = %s WHERE example_id = %s''',
                           (example.example_value, example.example_id))


        return ret_value, ret_code

    def delete_example(self, exampleId, user=None, auths=None):
        """
        fetches an example
        
        :param exampleId: ID of example to fetch
        :type exampleId: str

        :rtype: Example
        """
        ret_code = 200
        ret_value = None

        with self._connection:
          with self._connection.cursor() as cursor:
            cursor.execute('DELETE FROM example WHERE example_id = %s',
                   (exampleId,))
            if cursor.rowcount != 1:
                ret_code = 404

        return ret_value, ret_code

