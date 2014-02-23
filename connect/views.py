# Create your views here.
from mchacks import settings
from django.http import HttpResponse
import json


class JsonResponse(HttpResponse):
    def __init__(self, content={}, mimetype=None, status=None,
             content_type='application/json'):
        super(JsonResponse, self).__init__(json.dumps(content), mimetype=mimetype,
                                           status=status, content_type=content_type)

board = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
        ]

def place_move(request, col, player):
  global board
  col = int(col)
  player = int(player)
  index = 5
  for row in board:
    if board[index][col] == 0:
      board[index][col] = player
      break
    index = index - 1

  return JsonResponse({
      'board': board,
    })

def reset_game(request):
  global board
  board = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
        ]

  return JsonResponse({
      'board': board,
    })

def get_board(request):
  return JsonResponse({
      'board': board,
    })