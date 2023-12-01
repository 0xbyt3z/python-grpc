from concurrent import futures
from time import sleep

import grpc
import helloworld_pb2_grpc
import helloworld_pb2

from grpc_reflection.v1alpha import reflection

import sys

from auth import authenticate

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        authenticate(context)
        return helloworld_pb2.HelloReponse(message="Hello, %s!" % request.name)
    def SayHelloStreamResponse(self, request, context):
        authenticate(context)
        yield helloworld_pb2.HelloReponse(message=f"{request.name}, count with me !")
        for i in range(1,10):
            sleep(1)
            yield helloworld_pb2.HelloReponse(message="stream value %s!" % i)
    def SayHelloStreamRequest(self, request_iterator, context):
        names = []
        authenticate(context)
        for request in request_iterator:
            names.append(request.name)
        return helloworld_pb2.HelloReponse(message=f"{','.join(names)} are the names server recieved")

    def SayHelloBidiStream(self, request_iterator, context):
        authenticate(context)
        for request in request_iterator:
            yield helloworld_pb2.HelloReponse(message=f"Hello {request.name}")

    def DataTypes(self, request, context):
        print(sys.getsizeof(request.int32_value))
        
        return helloworld_pb2.DTResponse(value=request.bool_value)
    

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

    # add reflections 
    SERVICE_NAMES = (
        helloworld_pb2.DESCRIPTOR.services_by_name['Greeter'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()