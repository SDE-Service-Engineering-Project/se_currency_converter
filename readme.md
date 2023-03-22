# Generate proto sources

- Execute in root
  folder: `python -m grpc_tools.protoc -I ./proto --python_out=./generated --pyi_out=./generated --grpc_python_out=./generated proto/*.proto`
- Fix the import in `currency_service_pb2_grpc.py`:
    - From `import currency_service_pb2 as currency__service__pb2`
    - To `import generated.currency_service_pb2 as currency__service__pb2`
- Sadly, grpc/proto doesn't support relative paths, so this needs to be fixed after each re-generation of the code.


