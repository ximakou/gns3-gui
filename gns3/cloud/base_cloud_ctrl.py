# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Base cloud controller class.

Base class for interacting with Cloud APIs to create and manage cloud
instances.

"""


class BaseCloudCtrl(object):

    """ Base class for interacting with a cloud provider API. """

    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key

    def authenticate(self):
        raise NotImplementedError

    def create_instance(self, name, size, image, keypair):
        """ Create a new instance with the supplied attributes. """

        pass
        #self.

    def delete_instance(self, instance):
        """ Delete the specified instance.  Return True or False. """

        try:
            return self.driver.destroy_node(instance)

        except Exception as e:

            # libcloud raises generic 'Exception' with the error in the text
            if str(e) == "404 Not Found Instance could not be found":

                raise LookupError('Instance not found')

    def get_instance(self, instance):
        """ Return a Node object representing the requested instance. """

        for i in self.driver.list_nodes():
            if i.id == instance.id:
                return i

        return None

    def list_instances(self):
        """ Return a dict of instances in the current region ('id' as key). """

        return self.driver.list_nodes()

    def list_regions(self):
        raise NotImplementedError

    def terminate_instance(self, instance_id):
        raise NotImplementedError
