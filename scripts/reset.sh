#!/bin/bash
echo "🐣 Opening poetry shell"
source $(poetry env info --path)/bin/activate

echo "🛑 Stopping Evennia (server only)..."
evennia sstop

echo "🗑️ Deleting database..."
rm ./server/evennia.db3

echo "🗑️ Deleting logs..."
rm ./server/logs/*

echo "🏗️ Recreating database..."
evennia migrate

echo "✅ Starting Evennia..."
evennia start

echo "👀 Checking Evennia status..."
evennia status

echo "😄 Have fun!"
