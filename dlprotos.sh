#!/bin/bash
set -e
REPO=https://token.jfrog.io/token/libs-release/io/token
TOKEN_PROTOS_VER="1.1.120"
FANK_PROTOS_VER="1.2.0"
RPC_PROTOS_VER="1.0.124"

rm -rf ./protos
mkdir protos
echo "Fetching jars..."

wget $REPO/proto/tokenio-proto-external/$TOKEN_PROTOS_VER/tokenio-proto-external-$TOKEN_PROTOS_VER.jar
unzip -d protos/external -o tokenio-proto-external-$TOKEN_PROTOS_VER.jar 'gateway/*.proto'
rm tokenio-proto-external-$TOKEN_PROTOS_VER.jar

wget $REPO/proto/tokenio-proto-common/$TOKEN_PROTOS_VER/tokenio-proto-common-$TOKEN_PROTOS_VER.jar
unzip -d protos/common -o tokenio-proto-common-$TOKEN_PROTOS_VER.jar '*.proto'
unzip -d protos/common -o tokenio-proto-common-$TOKEN_PROTOS_VER.jar 'google/api/*.proto'
rm tokenio-proto-common-$TOKEN_PROTOS_VER.jar

wget $REPO/fank/tokenio-fank-proto/$FANK_PROTOS_VER/tokenio-fank-proto-$FANK_PROTOS_VER.jar
unzip -d protos -o tokenio-fank-proto-$FANK_PROTOS_VER.jar '*.proto'
rm tokenio-fank-proto-$FANK_PROTOS_VER.jar


wget $REPO/rpc/tokenio-rpc-proto/$RPC_PROTOS_VER/tokenio-rpc-proto-$RPC_PROTOS_VER.jar
unzip -d protos -o tokenio-rpc-proto-$RPC_PROTOS_VER.jar '*.proto'
rm tokenio-rpc-proto-$RPC_PROTOS_VER.jar
