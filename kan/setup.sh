#!/bin/bash
# 09.06.2025
docker pull ghcr.io/kanbn/kan:latest && docker run -it -p 3000:3000 --env-file .env ghcr.io/kanbn/kan:latest
