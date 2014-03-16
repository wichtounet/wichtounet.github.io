#!/bin/bash

sed -i 's/\[cpp\]/\`\`\`cpp\n/g' $1
sed -i 's/\[\/cpp\]/\n\`\`\`/g' $1