#!/bin/bash
if [[ $# -ne 2 ]] ; then
    echo 'Need to specify routes and port'
    exit 1
fi

ROUTES=$1
PORT=$2
traffic_port=$((PORT + 6000))
checkpoint_filename="${ROUTES#*/}"
checkpoint_filename="results_${checkpoint_filename%.*}_${PORT}.json"

echo "Evaluating without scenarios"
echo "Port ${PORT} and traffic port ${traffic_port}"
echo "Saving results in ${checkpoint_filename}"

source ~/miniconda3/etc/profile.d/conda.sh
conda activate LAV-env

python3 ${LEADERBOARD_ROOT}/leaderboard/leaderboard_evaluator.py \
--scenarios="/home/anthony/other_githubs/LAV/no_scenarios.json"  \
--routes=${ROUTES} \
--repetitions=${REPETITIONS} \
--track=${CHALLENGE_TRACK_CODENAME} \
--checkpoint=${checkpoint_filename} \
--agent=${TEAM_AGENT} \
--agent-config=${TEAM_CONFIG} \
--debug=${DEBUG_CHALLENGE} \
--record=${RECORD_PATH} \
--resume=${RESUME} \
--port=${PORT} \
--trafficManagerPort=${traffic_port}