from flask import current_app, session, render_template, request, jsonify, abort
from . import main
from ..models import Puzzle, Reward, Role, User
from .problem import problem
import random


@main.route('/')
def index():
    """Default application route."""

    parsons_problem = problem()
    random.shuffle(parsons_problem)

    return render_template('index.html', problem=parsons_problem)


@main.route('/check-solution', methods=['POST'])
def check_solution():
    """"""
    if request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        current_app.logger.debug(data)
#        feedback = [random.choice(['status-correct', 'status-wrong-tabs', 'status-wrong-line']) for line in data['answer']]
        parsons_problem = problem()
        feedback = []
        for answer, solution in zip(data['answer'], parsons_problem):
            current_app.logger.debug('Comparing lines {} and {}.'.format(answer['code-line'], solution[0]))
            current_app.logger.debug('Comparing tabs {} and {}.'.format(answer['num-tabs'], solution[2]))
            status = ''
            if int(answer['code-line']) == solution[0]:
                if int(answer['num-tabs']) == solution[2]:
                    status = 'status-correct'
                else:
                    status = 'status-wrong-tabs'
            else:
                status = 'status-wrong-line'
            feedback.append(status)

        return jsonify({'feedback': feedback})

    return jsonify({'error': 400}), 400
