import logging

from example_server.controllers.base_controller import BaseController


class ExampleController(BaseController):

    def create_example(self, example, user = None):
        """
        create_example
        Create a example
        :param example: 
        :type example: dict | bytes

        :rtype: Example
        """

        retcode = 200
        loc = None


        return loc, retcode


    def download_example(self, exampleId, user = None):
        """
        fetches an example
        
        :param exampleId: ID of example to fetch
        :type exampleId: str

        :rtype: Example
        """
        retcode = 200
        loc = None


        return loc, retcode


    def download_examples(self, studyName=None, start=None, count=None, orderby=None, user = None):
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
        retcode = 200
        loc = None

        cur = self._connection.cursor()

        cur.execute('SELECT id, example_value FROM example')

        for (eid, evalue) in cur:
            print ('row!')

        cur.close()

        return loc, retcode


    def update_example(self, exampleId, example, user = None):
        """
        updates an example
        
        :param exampleId: ID of example to update
        :type exampleId: str
        :param example: 
        :type example: dict | bytes

        :rtype: Example
        """

        retcode = 200
        loc = None

        return loc, retcode
