#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # list of movies to select from
        movies = ["The Big Lebowski", "Blue Velvet", "Toy Story", "Star Wars", "Amelie","Frozen","The Croods","Ice Age","How to Train Your Dragon","The Lion King"]

        # randomly choose one of the movies
        randomIdx = random.randrange(len(movies))


        return movies[randomIdx]


    def get(self):
        movie = self.getRandomMovie()
        movie2 = self.getRandomMovie()
        movie3 = self.getRandomMovie()

        # build the response string
        response = "<h1>Movie of the Day</h1>"
        response += "<ul><li>" + movie + "</li></ul>"

        response2 = "<h1>Today's movie</h1>"
        response2 += "<ul><li>" + movie2 + "</li></ul>"

        response3 = "<h1>Tomorrow's movie</h1>"
        response3 += "<ul><li>" + movie3 + "</li></ul>"



        self.response.write(response)
        self.response.write(response2)
        self.response.write(response3)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)


                              