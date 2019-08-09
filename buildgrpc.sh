#!/bin/bash
set -e

echo "Building grpc..."
PY_OUT=./tokenio/proto

rm -rf $PY_OUT
mkdir $PY_OUT
pipenv run python -m grpc.tools.protoc -I./protos/common -I./protos/external -I./protos --python_out=$PY_OUT --grpc_python_out=$PY_OUT ./protos/common/*.proto
pipenv run python -m grpc.tools.protoc -I./protos/common -I./protos/external -I./protos --python_out=$PY_OUT --grpc_python_out=$PY_OUT ./protos/external/gateway/*.proto
pipenv run python -m grpc.tools.protoc -I./protos/common -I./protos/external -I./protos --python_out=$PY_OUT --grpc_python_out=$PY_OUT ./protos/fank/*.proto
pipenv run python -m grpc.tools.protoc -I./protos/common -I./protos/external -I./protos --python_out=$PY_OUT --grpc_python_out=$PY_OUT ./protos/extensions/*.proto

find $PY_OUT -name \*.py -type f -exec \
    sed -i "" -E 's/^import (.*_pb2)/import tokenio.proto.\1/g' {} +
find $PY_OUT -name \*.py -type f -exec \
    sed -i "" -E 's/^from (extensions|gateway)/from tokenio.proto.\1/g' {} +
