from __future__ import print_function

import logging

import grpc
import helloworld_pb2_grpc
import helloworld_pb2
import random

def generate_requests():
    for i in range(5):
        yield helloworld_pb2.HelloRequest(name="a"*i)

def run():

    # unary
    # with grpc.insecure_channel("localhost:50051") as channel:
    #     stub = helloworld_pb2_grpc.GreeterStub(channel)
    #     response = stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
    # print("Greeter client received: " + response.message)


    # bidirectional
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        responses = stub.SayHelloBidiStream(generate_requests())
        for response in responses:
            print("Greeter client received: " + response.message)
            pass


if __name__ == "__main__":
    logging.basicConfig()
    run()