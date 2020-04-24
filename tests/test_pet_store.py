# Copyright (c) 2019 University of Illinois and others. All rights reserved.
#
# This program and the accompanying materials are made available under the
# terms of the Mozilla Public License v2.0 which accompanies this distribution,
# and is available at https://www.mozilla.org/en-US/MPL/2.0/

import requests


def test_get_pets():
    assert True


def test_get_pet():
    pet_id = 123
    response = requests.get(f"http://0.0.0.0:8080/pets/{pet_id}")
    assert response.status_code == 200


def test_delete_pet():
    assert True


def test_update_pet():
    assert True
