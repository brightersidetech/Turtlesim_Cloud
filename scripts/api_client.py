
import requests
import json
import time

server_update = "http://localhost:1026/v2/op/update"
server_create = "http://localhost:1026/v2/entities"

# get all entities
def get_status():
    r = requests.get(server)
    # Use a breakpoint in the code line below to debug your script.
    print(r.status_code)  # Press Ctrl+F8 to toggle the breakpoint.
    print(r.headers)
    print(r.content)
    my_json = json.loads(r.content)
    print(my_json)

# Create  entity
def create():
    data = {"id": ".turtle1.cmd_vel",
            "type": "geometry_msgs%2FTwist",
            "angular": {
                "type": "geometry_msgs%2FVector3",
                "value": {
                    "x": {
                        "value": 0,
                        "type": "number"
                    },
                    "y": {
                        "value": 0,
                        "type": "number"
                    },
                    "z": {
                        "value": 1,
                        "type": "number"
                    }
                },
                "metadata": {
                    "dataType": {
                        "type": "dataType",
                        "value": {
                            "x": "float64",
                            "y": "float64",
                            "z": "float64"
                        }
                    }
                }
            },
            "linear": {
                "type": "geometry_msgs%2FVector3",
                "value": {
                    "x": {
                        "value": 1,
                        "type": "number"
                    },
                    "y": {
                        "value": 0,
                        "type": "number"
                    },
                    "z": {
                        "value": 0,
                        "type": "number"
                    }
                },
                "metadata": {
                    "dataType": {
                        "type": "dataType",
                        "value": {
                            "x": "float64",
                            "y": "float64",
                            "z": "float64"
                        }
                    }
                }
            }
        }
    headers = {"Content-Type": "application/json"}
    r = requests.post(server_create, data=json.dumps(data), headers=headers)
    print(r.status_code)
    request_status("post", r.status_code)

# display request status message
def request_status(method, code):
    if method == "post" and code == 201:
        print("Entity has been created")

def update():
    data =  {"actionType": "update",
            "entities": [ 
            {
                    "id": ".turtle1.cmd_vel",
                    "type": "geometry_msgs%2FTwist",
                    "angular": {
                        "type": "geometry_msgs%2FVector3",
                        "value": {
                            "x": {
                                "value": 0,
                                "type": "number"
                            },
                            "y": {
                                "value": 0,
                                "type": "number"
                            },
                            "z": {
                                "value": 1,
                                "type": "number"
                            }
                        },
                        "metadata": {
                            "dataType": {
                                "type": "dataType",
                                "value": {
                                    "x": "float64",
                                    "y": "float64",
                                    "z": "float64"
                                }
                            }
                        }
                    },
                    "linear": {
                        "type": "geometry_msgs%2FVector3",
                        "value": {
                            "x": {
                                "value": 1,
                                "type": "number"
                            },
                            "y": {
                                "value": 0,
                                "type": "number"
                            },
                            "z": {
                                "value": 0,
                                "type": "number"
                            }
                        },
                        "metadata": {
                            "dataType": {
                                "type": "dataType",
                                "value": {
                                    "x": "float64",
                                    "y": "float64",
                                    "z": "float64"
                                }
                            }
                        }
                    }
                }
            ]
        }
    headers = {"Content-Type": "application/json"}
    r = requests.post(server_update, data=json.dumps(data), headers=headers)
    print(r.status_code)
    #request_status("post", r.status_code)


if __name__ == '__main__':
    #get_status()
    update()