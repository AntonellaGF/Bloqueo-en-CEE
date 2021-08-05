#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on agosto 03, 2021, at 19:09
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'tesis'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Tesis 2021\\Bloqueo-en-CEE\\Psycopy\\tesis_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "intro"
introClock = core.Clock()
intro1 = visual.TextStim(win=win, name='intro1',
    text='Este estudio consta dos partes. A lo largo del mismo vas a ir aprendiendo cosas. Es necesario que prestes atención a los estimulos que se te van a ir presentando en pantalla.\n\nAl finalizar, te vamos a hacer algunas preguntas personales. Es importante que sepas que las respuestas serán tratadas de manera confidencial. Los resultados obtenidos de esta investigación, serán comunicados en eventos científicos y publicados en revistas científicas. \n\nAPRETA LA BARRA ESPACIADORA PARA CONTINUAR ',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "intro2"
intro2Clock = core.Clock()
introduccion2 = visual.TextStim(win=win, name='introduccion2',
    text='Tu participación es voluntaria: \npodés rehusarte a participar o interrumpir tu participación en cualquier momento sin tener que expresar tus razones con el boton "esc".\n\n\nAPRETA LA BARRA ESPACIADORA PARA CONTINUAR ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "indicaciones"
indicacionesClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "entrenamiento1"
entrenamiento1Clock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.3, -0.05), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=0.0, pos=(0.3, -0.05), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
flechas = keyboard.Keyboard()
crux = visual.TextStim(win=win, name='crux',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
puntitos = list()
contador = 0

# Initialize components for Routine "feddback"
feddbackClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "entrenamiento2"
entrenamiento2Clock = core.Clock()
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.3), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.3, -0.05), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='sin', mask=None,
    ori=0.0, pos=(0.3, -0.05), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
flechas_3 = keyboard.Keyboard()
crux_3 = visual.TextStim(win=win, name='crux_3',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
contador2 = 0
puntitos2 = list()

# Initialize components for Routine "feedback2"
feedback2Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "entrenamiento3"
entrenamiento3Clock = core.Clock()
image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.3), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.3, -0.05), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='sin', mask=None,
    ori=0.0, pos=(0.3, -0.05), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
flechas_4 = keyboard.Keyboard()
crux_4 = visual.TextStim(win=win, name='crux_4',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
contador3 = 0
puntitos3 = list()

# Initialize components for Routine "feedback3"
feedback3Clock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pausa"
pausaClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='PAUSA\n\n\nTomese un tiempo para descansar la vista. \nCuando este listo presione la barra espaciadora para continuar.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "testeo"
testeoClock = core.Clock()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.3, -0.05), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='sin', mask=None,
    ori=0.0, pos=(0.3, -0.05), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
flechas_2 = keyboard.Keyboard()
crux_2 = visual.TextStim(win=win, name='crux_2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "fedbackteste1"
fedbackteste1Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testeo2"
testeo2Clock = core.Clock()
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.3, -0.05), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='sin', mask=None,
    ori=0.0, pos=(0.3, -0.05), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
flechas_5 = keyboard.Keyboard()
crux_5 = visual.TextStim(win=win, name='crux_5',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "feedbackteste2"
feedbackteste2Clock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "final"
finalClock = core.Clock()
final1 = visual.TextStim(win=win, name='final1',
    text='Hemos finalizado el experimento.\n\nGracias por participar del mismo, ahora le haremos un par de preguntas.\n\nLa calidad de nuestra investigación depende de la calidad de los datos que obtengamos. \nPor favor, respondé con sinceridad si podemos contar con tus respuestas.\n\nAPRETA BARRA ESPACIADORA PARA CONTINUAR ',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "pregunta1"
pregunta1Clock = core.Clock()
preg1 = visual.TextStim(win=win, name='preg1',
    text='¿Hay algo que ocurrió durante el experimento que nos quieras comunicar o que necesitemos saber?  Por favor, escribilo acá abajo. \n\n"Por ejemplo: tuve que atender el telefono"\n\nAl finalizar apreta 1\n\n',
    font='Open Sans',
    pos=(0, 0.05), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()
textbox = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -0.3),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=(0.8824, 0.9451, 1.0000),
     flipHoriz=False, flipVert=False,
     editable=True,
     name='textbox',
     autoLog=True,
)

# Initialize components for Routine "pregunta2"
pregunta2Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()
button = visual.ButtonStim(win, 
   text='', font='Arvo',
   pos=(0, -0.2),
   letterHeight=0.05,
   size=None, borderWidth=0.0,
   fillColor='darkgrey', borderColor=(0.9216, 0.9216, 0.9216),
   color='white', colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='button')
button.buttonClock = core.Clock()
button_2 = visual.ButtonStim(win, 
   text='NO', font='Arvo',
   pos=(0, -0.3),
   letterHeight=0.05,
   size=None, borderWidth=0.0,
   fillColor='darkgrey', borderColor=(0.9216, 0.9216, 0.9216),
   color='white', colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='button_2')
button_2.buttonClock = core.Clock()

# Initialize components for Routine "final_2"
final_2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Muchas gracias por completar el experimento.\nÉste tiene como objetivo investigar sobre el aprendizaje de conceptos en las personas. \nTus resultados ayudarán a comprender mejor estos temas, ademas de estar ayudando a la realización de una tesis.\n\nApreta la barra espaciadora para finalizar ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
introComponents = [intro1, key_resp]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro1* updates
    if intro1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro1.frameNStart = frameN  # exact frame index
        intro1.tStart = t  # local t and not account for scr refresh
        intro1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro1, 'tStartRefresh')  # time at next scr refresh
        intro1.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intro1.started', intro1.tStartRefresh)
thisExp.addData('intro1.stopped', intro1.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "intro2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
intro2Components = [introduccion2, key_resp_2]
for thisComponent in intro2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro2"-------
while continueRoutine:
    # get current time
    t = intro2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduccion2* updates
    if introduccion2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduccion2.frameNStart = frameN  # exact frame index
        introduccion2.tStart = t  # local t and not account for scr refresh
        introduccion2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduccion2, 'tStartRefresh')  # time at next scr refresh
        introduccion2.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro2"-------
for thisComponent in intro2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introduccion2.started', introduccion2.tStartRefresh)
thisExp.addData('introduccion2.stopped', introduccion2.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "intro2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "indicaciones"-------
continueRoutine = True
# update component parameters for each repeat
text_7.setText('En el experimento vas a tener que apretar las flechas izquierda y derecha para elegir la opcion correcta. Tenes un limite de 3 segundos para responder\n\nAPRETA LA BARRA ESPACIADORA PARA CONTINUAR ')
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
indicacionesComponents = [text_7, key_resp_7]
for thisComponent in indicacionesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
indicacionesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "indicaciones"-------
while continueRoutine:
    # get current time
    t = indicacionesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=indicacionesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in indicacionesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "indicaciones"-------
for thisComponent in indicacionesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
# the Routine "indicaciones" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=8.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('entrenamiento1.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "entrenamiento1"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    image.setImage(muestra)
    image_2.setImage(comp1)
    image_3.setImage(comp2)
    flechas.keys = []
    flechas.rt = []
    _flechas_allKeys = []
    # keep track of which components have finished
    entrenamiento1Components = [image, image_2, image_3, flechas, crux]
    for thisComponent in entrenamiento1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    entrenamiento1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "entrenamiento1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = entrenamiento1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=entrenamiento1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        if image_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                image_2.setAutoDraw(False)
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            image_3.setAutoDraw(True)
        if image_3.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                image_3.tStop = t  # not accounting for scr refresh
                image_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                image_3.setAutoDraw(False)
        
        # *flechas* updates
        waitOnFlip = False
        if flechas.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            flechas.frameNStart = frameN  # exact frame index
            flechas.tStart = t  # local t and not account for scr refresh
            flechas.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(flechas, 'tStartRefresh')  # time at next scr refresh
            flechas.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(flechas.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(flechas.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if flechas.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                flechas.tStop = t  # not accounting for scr refresh
                flechas.frameNStop = frameN  # exact frame index
                win.timeOnFlip(flechas, 'tStopRefresh')  # time at next scr refresh
                flechas.status = FINISHED
        if flechas.status == STARTED and not waitOnFlip:
            theseKeys = flechas.getKeys(keyList=['left', 'right'], waitRelease=False)
            _flechas_allKeys.extend(theseKeys)
            if len(_flechas_allKeys):
                flechas.keys = _flechas_allKeys[-1].name  # just the last key pressed
                flechas.rt = _flechas_allKeys[-1].rt
                # was this correct?
                if (flechas.keys == str(correct_key)) or (flechas.keys == correct_key):
                    flechas.corr = 1
                else:
                    flechas.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *crux* updates
        if crux.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crux.frameNStart = frameN  # exact frame index
            crux.tStart = t  # local t and not account for scr refresh
            crux.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crux, 'tStartRefresh')  # time at next scr refresh
            crux.setAutoDraw(True)
        if crux.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 1.0-frameTolerance:
                # keep track of stop time/frame for later
                crux.tStop = t  # not accounting for scr refresh
                crux.frameNStop = frameN  # exact frame index
                win.timeOnFlip(crux, 'tStopRefresh')  # time at next scr refresh
                crux.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in entrenamiento1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "entrenamiento1"-------
    for thisComponent in entrenamiento1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    trials.addData('image_2.started', image_2.tStartRefresh)
    trials.addData('image_2.stopped', image_2.tStopRefresh)
    trials.addData('image_3.started', image_3.tStartRefresh)
    trials.addData('image_3.stopped', image_3.tStopRefresh)
    # check responses
    if flechas.keys in ['', [], None]:  # No response was made
        flechas.keys = None
        # was no response the correct answer?!
        if str(correct_key).lower() == 'none':
           flechas.corr = 1;  # correct non-response
        else:
           flechas.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('flechas.keys',flechas.keys)
    trials.addData('flechas.corr', flechas.corr)
    if flechas.keys != None:  # we had a response
        trials.addData('flechas.rt', flechas.rt)
    trials.addData('flechas.started', flechas.tStartRefresh)
    trials.addData('flechas.stopped', flechas.tStopRefresh)
    trials.addData('crux.started', crux.tStartRefresh)
    trials.addData('crux.stopped', crux.tStopRefresh)
    contador += 1
    if not flechas.keys:
        feedback = "muy lento!"
    elif flechas.keys == str(correct_key):
        feedback = "bien hecho :)"
        puntitos.append(1)
    else:
        feedback = "error :("
        puntitos.append(0)
    
    # ------Prepare to start Routine "feddback"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    text_3.setText(feedback)
    # keep track of which components have finished
    feddbackComponents = [text_3]
    for thisComponent in feddbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feddbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feddback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feddbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feddbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feddbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feddback"-------
    for thisComponent in feddbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_3.started', text_3.tStartRefresh)
    trials.addData('text_3.stopped', text_3.tStopRefresh)
    if contador >= 30:
        if sum(puntitos[-28:])/30 >= 0.93:
            trials.finished = True
    thisExp.nextEntry()
    
# completed 8.0 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=8.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('entrenamiento2.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "entrenamiento2"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    image_7.setSize((0.4, 0.2))
    image_7.setImage(muestra)
    image_8.setImage(comp1)
    image_9.setImage(comp2)
    flechas_3.keys = []
    flechas_3.rt = []
    _flechas_3_allKeys = []
    # keep track of which components have finished
    entrenamiento2Components = [image_7, image_8, image_9, flechas_3, crux_3]
    for thisComponent in entrenamiento2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    entrenamiento2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "entrenamiento2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = entrenamiento2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=entrenamiento2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_7* updates
        if image_7.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image_7.frameNStart = frameN  # exact frame index
            image_7.tStart = t  # local t and not account for scr refresh
            image_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
            image_7.setAutoDraw(True)
        if image_7.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                image_7.tStop = t  # not accounting for scr refresh
                image_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_7, 'tStopRefresh')  # time at next scr refresh
                image_7.setAutoDraw(False)
        
        # *image_8* updates
        if image_8.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image_8.frameNStart = frameN  # exact frame index
            image_8.tStart = t  # local t and not account for scr refresh
            image_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
            image_8.setAutoDraw(True)
        if image_8.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                image_8.tStop = t  # not accounting for scr refresh
                image_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_8, 'tStopRefresh')  # time at next scr refresh
                image_8.setAutoDraw(False)
        
        # *image_9* updates
        if image_9.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image_9.frameNStart = frameN  # exact frame index
            image_9.tStart = t  # local t and not account for scr refresh
            image_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
            image_9.setAutoDraw(True)
        if image_9.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                image_9.tStop = t  # not accounting for scr refresh
                image_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_9, 'tStopRefresh')  # time at next scr refresh
                image_9.setAutoDraw(False)
        
        # *flechas_3* updates
        waitOnFlip = False
        if flechas_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            flechas_3.frameNStart = frameN  # exact frame index
            flechas_3.tStart = t  # local t and not account for scr refresh
            flechas_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(flechas_3, 'tStartRefresh')  # time at next scr refresh
            flechas_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(flechas_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(flechas_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if flechas_3.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                flechas_3.tStop = t  # not accounting for scr refresh
                flechas_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(flechas_3, 'tStopRefresh')  # time at next scr refresh
                flechas_3.status = FINISHED
        if flechas_3.status == STARTED and not waitOnFlip:
            theseKeys = flechas_3.getKeys(keyList=['left', 'right'], waitRelease=False)
            _flechas_3_allKeys.extend(theseKeys)
            if len(_flechas_3_allKeys):
                flechas_3.keys = _flechas_3_allKeys[-1].name  # just the last key pressed
                flechas_3.rt = _flechas_3_allKeys[-1].rt
                # was this correct?
                if (flechas_3.keys == str(correct_key)) or (flechas_3.keys == correct_key):
                    flechas_3.corr = 1
                else:
                    flechas_3.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *crux_3* updates
        if crux_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crux_3.frameNStart = frameN  # exact frame index
            crux_3.tStart = t  # local t and not account for scr refresh
            crux_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crux_3, 'tStartRefresh')  # time at next scr refresh
            crux_3.setAutoDraw(True)
        if crux_3.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 1.0-frameTolerance:
                # keep track of stop time/frame for later
                crux_3.tStop = t  # not accounting for scr refresh
                crux_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(crux_3, 'tStopRefresh')  # time at next scr refresh
                crux_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in entrenamiento2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "entrenamiento2"-------
    for thisComponent in entrenamiento2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('image_7.started', image_7.tStartRefresh)
    trials_3.addData('image_7.stopped', image_7.tStopRefresh)
    trials_3.addData('image_8.started', image_8.tStartRefresh)
    trials_3.addData('image_8.stopped', image_8.tStopRefresh)
    trials_3.addData('image_9.started', image_9.tStartRefresh)
    trials_3.addData('image_9.stopped', image_9.tStopRefresh)
    # check responses
    if flechas_3.keys in ['', [], None]:  # No response was made
        flechas_3.keys = None
        # was no response the correct answer?!
        if str(correct_key).lower() == 'none':
           flechas_3.corr = 1;  # correct non-response
        else:
           flechas_3.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('flechas_3.keys',flechas_3.keys)
    trials_3.addData('flechas_3.corr', flechas_3.corr)
    if flechas_3.keys != None:  # we had a response
        trials_3.addData('flechas_3.rt', flechas_3.rt)
    trials_3.addData('flechas_3.started', flechas_3.tStartRefresh)
    trials_3.addData('flechas_3.stopped', flechas_3.tStopRefresh)
    trials_3.addData('crux_3.started', crux_3.tStartRefresh)
    trials_3.addData('crux_3.stopped', crux_3.tStopRefresh)
    contador2 += 1
    if not flechas_3.keys:
        feedback = "muy lento!"
    elif flechas_3.keys == str(correct_key):
        feedback = "bien hecho :)"
        puntitos2.append(1)
    else:
        feedback = "error :("
        puntitos2.append(0)
    
    # ------Prepare to start Routine "feedback2"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    text_5.setText(feedback)
    # keep track of which components have finished
    feedback2Components = [text_5]
    for thisComponent in feedback2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedback2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedback2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedback2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback2"-------
    for thisComponent in feedback2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('text_5.started', text_5.tStartRefresh)
    trials_3.addData('text_5.stopped', text_5.tStopRefresh)
    if contador2 >= 30:
        if sum(puntitos2[-28:])/30 >= 0.93:
            trials3.finished = True
    thisExp.nextEntry()
    
# completed 8.0 repeats of 'trials_3'


# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('entrenamiento3.xlsx'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "entrenamiento3"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    image_10.setSize((0.4, 0.2))
    image_10.setImage(muestra)
    image_11.setImage(comp1)
    image_12.setImage(comp2)
    flechas_4.keys = []
    flechas_4.rt = []
    _flechas_4_allKeys = []
    # keep track of which components have finished
    entrenamiento3Components = [image_10, image_11, image_12, flechas_4, crux_4]
    for thisComponent in entrenamiento3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    entrenamiento3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "entrenamiento3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = entrenamiento3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=entrenamiento3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_10* updates
        if image_10.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image_10.frameNStart = frameN  # exact frame index
            image_10.tStart = t  # local t and not account for scr refresh
            image_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
            image_10.setAutoDraw(True)
        if image_10.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                image_10.tStop = t  # not accounting for scr refresh
                image_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_10, 'tStopRefresh')  # time at next scr refresh
                image_10.setAutoDraw(False)
        
        # *image_11* updates
        if image_11.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image_11.frameNStart = frameN  # exact frame index
            image_11.tStart = t  # local t and not account for scr refresh
            image_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
            image_11.setAutoDraw(True)
        if image_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                image_11.tStop = t  # not accounting for scr refresh
                image_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_11, 'tStopRefresh')  # time at next scr refresh
                image_11.setAutoDraw(False)
        
        # *image_12* updates
        if image_12.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image_12.frameNStart = frameN  # exact frame index
            image_12.tStart = t  # local t and not account for scr refresh
            image_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
            image_12.setAutoDraw(True)
        if image_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                image_12.tStop = t  # not accounting for scr refresh
                image_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_12, 'tStopRefresh')  # time at next scr refresh
                image_12.setAutoDraw(False)
        
        # *flechas_4* updates
        waitOnFlip = False
        if flechas_4.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            flechas_4.frameNStart = frameN  # exact frame index
            flechas_4.tStart = t  # local t and not account for scr refresh
            flechas_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(flechas_4, 'tStartRefresh')  # time at next scr refresh
            flechas_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(flechas_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(flechas_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if flechas_4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                flechas_4.tStop = t  # not accounting for scr refresh
                flechas_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(flechas_4, 'tStopRefresh')  # time at next scr refresh
                flechas_4.status = FINISHED
        if flechas_4.status == STARTED and not waitOnFlip:
            theseKeys = flechas_4.getKeys(keyList=['left', 'right'], waitRelease=False)
            _flechas_4_allKeys.extend(theseKeys)
            if len(_flechas_4_allKeys):
                flechas_4.keys = _flechas_4_allKeys[-1].name  # just the last key pressed
                flechas_4.rt = _flechas_4_allKeys[-1].rt
                # was this correct?
                if (flechas_4.keys == str(correct_key)) or (flechas_4.keys == correct_key):
                    flechas_4.corr = 1
                else:
                    flechas_4.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *crux_4* updates
        if crux_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crux_4.frameNStart = frameN  # exact frame index
            crux_4.tStart = t  # local t and not account for scr refresh
            crux_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crux_4, 'tStartRefresh')  # time at next scr refresh
            crux_4.setAutoDraw(True)
        if crux_4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 1.0-frameTolerance:
                # keep track of stop time/frame for later
                crux_4.tStop = t  # not accounting for scr refresh
                crux_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(crux_4, 'tStopRefresh')  # time at next scr refresh
                crux_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in entrenamiento3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "entrenamiento3"-------
    for thisComponent in entrenamiento3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_4.addData('image_10.started', image_10.tStartRefresh)
    trials_4.addData('image_10.stopped', image_10.tStopRefresh)
    trials_4.addData('image_11.started', image_11.tStartRefresh)
    trials_4.addData('image_11.stopped', image_11.tStopRefresh)
    trials_4.addData('image_12.started', image_12.tStartRefresh)
    trials_4.addData('image_12.stopped', image_12.tStopRefresh)
    # check responses
    if flechas_4.keys in ['', [], None]:  # No response was made
        flechas_4.keys = None
        # was no response the correct answer?!
        if str(correct_key).lower() == 'none':
           flechas_4.corr = 1;  # correct non-response
        else:
           flechas_4.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_4 (TrialHandler)
    trials_4.addData('flechas_4.keys',flechas_4.keys)
    trials_4.addData('flechas_4.corr', flechas_4.corr)
    if flechas_4.keys != None:  # we had a response
        trials_4.addData('flechas_4.rt', flechas_4.rt)
    trials_4.addData('flechas_4.started', flechas_4.tStartRefresh)
    trials_4.addData('flechas_4.stopped', flechas_4.tStopRefresh)
    trials_4.addData('crux_4.started', crux_4.tStartRefresh)
    trials_4.addData('crux_4.stopped', crux_4.tStopRefresh)
    contador3 += 1
    if not flechas_4.keys:
        feedback = "muy lento!"
    elif flechas_4.keys == str(correct_key):
        feedback = "bien hecho :)"
        puntitos3.append(1)
    else:
        feedback = "error :("
        puntitos3.append(0)
    
    # ------Prepare to start Routine "feedback3"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    text_6.setText(feedback)
    # keep track of which components have finished
    feedback3Components = [text_6]
    for thisComponent in feedback3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedback3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedback3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedback3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback3"-------
    for thisComponent in feedback3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_4.addData('text_6.started', text_6.tStartRefresh)
    trials_4.addData('text_6.stopped', text_6.tStopRefresh)
    if contador3 >= 30:
        if sum(puntitos3[-28:])/30 >= 0.93:
            trials4.finished = True
# completed 0.0 repeats of 'trials_4'


# ------Prepare to start Routine "pausa"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
pausaComponents = [text_9, key_resp_8]
for thisComponent in pausaComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pausaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pausa"-------
while continueRoutine:
    # get current time
    t = pausaClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pausaClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pausaComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pausa"-------
for thisComponent in pausaComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "pausa" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('testeo1.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testeo"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    image_4.setImage(muestra)
    image_5.setImage(comp1)
    image_6.setImage(comp2)
    flechas_2.keys = []
    flechas_2.rt = []
    _flechas_2_allKeys = []
    # keep track of which components have finished
    testeoComponents = [image_4, image_5, image_6, flechas_2, crux_2]
    for thisComponent in testeoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testeoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testeo"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testeoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testeoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_4* updates
        if image_4.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image_4.frameNStart = frameN  # exact frame index
            image_4.tStart = t  # local t and not account for scr refresh
            image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
            image_4.setAutoDraw(True)
        if image_4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                image_4.tStop = t  # not accounting for scr refresh
                image_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
                image_4.setAutoDraw(False)
        
        # *image_5* updates
        if image_5.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image_5.frameNStart = frameN  # exact frame index
            image_5.tStart = t  # local t and not account for scr refresh
            image_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
            image_5.setAutoDraw(True)
        if image_5.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                image_5.tStop = t  # not accounting for scr refresh
                image_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_5, 'tStopRefresh')  # time at next scr refresh
                image_5.setAutoDraw(False)
        
        # *image_6* updates
        if image_6.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image_6.frameNStart = frameN  # exact frame index
            image_6.tStart = t  # local t and not account for scr refresh
            image_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
            image_6.setAutoDraw(True)
        if image_6.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                image_6.tStop = t  # not accounting for scr refresh
                image_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_6, 'tStopRefresh')  # time at next scr refresh
                image_6.setAutoDraw(False)
        
        # *flechas_2* updates
        waitOnFlip = False
        if flechas_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            flechas_2.frameNStart = frameN  # exact frame index
            flechas_2.tStart = t  # local t and not account for scr refresh
            flechas_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(flechas_2, 'tStartRefresh')  # time at next scr refresh
            flechas_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(flechas_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(flechas_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if flechas_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                flechas_2.tStop = t  # not accounting for scr refresh
                flechas_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(flechas_2, 'tStopRefresh')  # time at next scr refresh
                flechas_2.status = FINISHED
        if flechas_2.status == STARTED and not waitOnFlip:
            theseKeys = flechas_2.getKeys(keyList=['left', 'right'], waitRelease=False)
            _flechas_2_allKeys.extend(theseKeys)
            if len(_flechas_2_allKeys):
                flechas_2.keys = _flechas_2_allKeys[-1].name  # just the last key pressed
                flechas_2.rt = _flechas_2_allKeys[-1].rt
                # was this correct?
                if (flechas_2.keys == str(correcta)) or (flechas_2.keys == correcta):
                    flechas_2.corr = 1
                else:
                    flechas_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *crux_2* updates
        if crux_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crux_2.frameNStart = frameN  # exact frame index
            crux_2.tStart = t  # local t and not account for scr refresh
            crux_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crux_2, 'tStartRefresh')  # time at next scr refresh
            crux_2.setAutoDraw(True)
        if crux_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 1.0-frameTolerance:
                # keep track of stop time/frame for later
                crux_2.tStop = t  # not accounting for scr refresh
                crux_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(crux_2, 'tStopRefresh')  # time at next scr refresh
                crux_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testeoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testeo"-------
    for thisComponent in testeoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('image_4.started', image_4.tStartRefresh)
    trials_2.addData('image_4.stopped', image_4.tStopRefresh)
    trials_2.addData('image_5.started', image_5.tStartRefresh)
    trials_2.addData('image_5.stopped', image_5.tStopRefresh)
    trials_2.addData('image_6.started', image_6.tStartRefresh)
    trials_2.addData('image_6.stopped', image_6.tStopRefresh)
    # check responses
    if flechas_2.keys in ['', [], None]:  # No response was made
        flechas_2.keys = None
        # was no response the correct answer?!
        if str(correcta).lower() == 'none':
           flechas_2.corr = 1;  # correct non-response
        else:
           flechas_2.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('flechas_2.keys',flechas_2.keys)
    trials_2.addData('flechas_2.corr', flechas_2.corr)
    if flechas_2.keys != None:  # we had a response
        trials_2.addData('flechas_2.rt', flechas_2.rt)
    trials_2.addData('flechas_2.started', flechas_2.tStartRefresh)
    trials_2.addData('flechas_2.stopped', flechas_2.tStopRefresh)
    trials_2.addData('crux_2.started', crux_2.tStartRefresh)
    trials_2.addData('crux_2.stopped', crux_2.tStopRefresh)
    if not flechas_2.keys:
        feedback = "muy lento!"
        duracionn = 1
    #elif flechas_2.keys == str(correcta):
        #feedback = "bien hecho :)"
    else:
        feedback = "++"
        duracionn = 0
    
    # ------Prepare to start Routine "fedbackteste1"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_4.setText(feedback)
    # keep track of which components have finished
    fedbackteste1Components = [text_4]
    for thisComponent in fedbackteste1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fedbackteste1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fedbackteste1"-------
    while continueRoutine:
        # get current time
        t = fedbackteste1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fedbackteste1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + duracionn-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fedbackteste1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fedbackteste1"-------
    for thisComponent in fedbackteste1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('text_4.started', text_4.tStartRefresh)
    trials_2.addData('text_4.stopped', text_4.tStopRefresh)
    # the Routine "fedbackteste1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('testeo2.xlsx'),
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5:
        exec('{} = thisTrial_5[paramName]'.format(paramName))

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testeo2"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    image_13.setImage(muestra)
    image_14.setImage(comp1)
    image_15.setImage(comp2)
    flechas_5.keys = []
    flechas_5.rt = []
    _flechas_5_allKeys = []
    # keep track of which components have finished
    testeo2Components = [image_13, image_14, image_15, flechas_5, crux_5]
    for thisComponent in testeo2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testeo2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testeo2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testeo2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testeo2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_13* updates
        if image_13.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image_13.frameNStart = frameN  # exact frame index
            image_13.tStart = t  # local t and not account for scr refresh
            image_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
            image_13.setAutoDraw(True)
        if image_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                image_13.tStop = t  # not accounting for scr refresh
                image_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_13, 'tStopRefresh')  # time at next scr refresh
                image_13.setAutoDraw(False)
        
        # *image_14* updates
        if image_14.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image_14.frameNStart = frameN  # exact frame index
            image_14.tStart = t  # local t and not account for scr refresh
            image_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
            image_14.setAutoDraw(True)
        if image_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                image_14.tStop = t  # not accounting for scr refresh
                image_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_14, 'tStopRefresh')  # time at next scr refresh
                image_14.setAutoDraw(False)
        
        # *image_15* updates
        if image_15.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            image_15.frameNStart = frameN  # exact frame index
            image_15.tStart = t  # local t and not account for scr refresh
            image_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
            image_15.setAutoDraw(True)
        if image_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                image_15.tStop = t  # not accounting for scr refresh
                image_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_15, 'tStopRefresh')  # time at next scr refresh
                image_15.setAutoDraw(False)
        
        # *flechas_5* updates
        waitOnFlip = False
        if flechas_5.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            flechas_5.frameNStart = frameN  # exact frame index
            flechas_5.tStart = t  # local t and not account for scr refresh
            flechas_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(flechas_5, 'tStartRefresh')  # time at next scr refresh
            flechas_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(flechas_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(flechas_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if flechas_5.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4.0-frameTolerance:
                # keep track of stop time/frame for later
                flechas_5.tStop = t  # not accounting for scr refresh
                flechas_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(flechas_5, 'tStopRefresh')  # time at next scr refresh
                flechas_5.status = FINISHED
        if flechas_5.status == STARTED and not waitOnFlip:
            theseKeys = flechas_5.getKeys(keyList=['left', 'right'], waitRelease=False)
            _flechas_5_allKeys.extend(theseKeys)
            if len(_flechas_5_allKeys):
                flechas_5.keys = _flechas_5_allKeys[-1].name  # just the last key pressed
                flechas_5.rt = _flechas_5_allKeys[-1].rt
                # was this correct?
                if (flechas_5.keys == str(correcta)) or (flechas_5.keys == correcta):
                    flechas_5.corr = 1
                else:
                    flechas_5.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *crux_5* updates
        if crux_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crux_5.frameNStart = frameN  # exact frame index
            crux_5.tStart = t  # local t and not account for scr refresh
            crux_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crux_5, 'tStartRefresh')  # time at next scr refresh
            crux_5.setAutoDraw(True)
        if crux_5.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 1.0-frameTolerance:
                # keep track of stop time/frame for later
                crux_5.tStop = t  # not accounting for scr refresh
                crux_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(crux_5, 'tStopRefresh')  # time at next scr refresh
                crux_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testeo2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testeo2"-------
    for thisComponent in testeo2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_5.addData('image_13.started', image_13.tStartRefresh)
    trials_5.addData('image_13.stopped', image_13.tStopRefresh)
    trials_5.addData('image_14.started', image_14.tStartRefresh)
    trials_5.addData('image_14.stopped', image_14.tStopRefresh)
    trials_5.addData('image_15.started', image_15.tStartRefresh)
    trials_5.addData('image_15.stopped', image_15.tStopRefresh)
    # check responses
    if flechas_5.keys in ['', [], None]:  # No response was made
        flechas_5.keys = None
        # was no response the correct answer?!
        if str(correcta).lower() == 'none':
           flechas_5.corr = 1;  # correct non-response
        else:
           flechas_5.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_5 (TrialHandler)
    trials_5.addData('flechas_5.keys',flechas_5.keys)
    trials_5.addData('flechas_5.corr', flechas_5.corr)
    if flechas_5.keys != None:  # we had a response
        trials_5.addData('flechas_5.rt', flechas_5.rt)
    trials_5.addData('flechas_5.started', flechas_5.tStartRefresh)
    trials_5.addData('flechas_5.stopped', flechas_5.tStopRefresh)
    trials_5.addData('crux_5.started', crux_5.tStartRefresh)
    trials_5.addData('crux_5.stopped', crux_5.tStopRefresh)
    if not flechas_5.keys:
        feedback = "muy lento!"
        duracionn = 1
    #elif flechas_5.keys == str(correcta):
        #feedback = "bien hecho :)"
    else:
        feedback = "++"
        duracionn = 0
    
    # ------Prepare to start Routine "feedbackteste2"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_8.setText(feedback)
    # keep track of which components have finished
    feedbackteste2Components = [text_8]
    for thisComponent in feedbackteste2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackteste2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackteste2"-------
    while continueRoutine:
        # get current time
        t = feedbackteste2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackteste2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + duracionn-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackteste2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackteste2"-------
    for thisComponent in feedbackteste2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_5.addData('text_8.started', text_8.tStartRefresh)
    trials_5.addData('text_8.stopped', text_8.tStopRefresh)
    # the Routine "feedbackteste2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_5'


# ------Prepare to start Routine "final"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
finalComponents = [final1, key_resp_3]
for thisComponent in finalComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "final"-------
while continueRoutine:
    # get current time
    t = finalClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finalClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *final1* updates
    if final1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        final1.frameNStart = frameN  # exact frame index
        final1.tStart = t  # local t and not account for scr refresh
        final1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(final1, 'tStartRefresh')  # time at next scr refresh
        final1.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "final"-------
for thisComponent in finalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('final1.started', final1.tStartRefresh)
thisExp.addData('final1.stopped', final1.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "final" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "pregunta1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
pregunta1Components = [preg1, key_resp_4, textbox]
for thisComponent in pregunta1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pregunta1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pregunta1"-------
while continueRoutine:
    # get current time
    t = pregunta1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pregunta1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *preg1* updates
    if preg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        preg1.frameNStart = frameN  # exact frame index
        preg1.tStart = t  # local t and not account for scr refresh
        preg1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(preg1, 'tStartRefresh')  # time at next scr refresh
        preg1.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['1'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *textbox* updates
    if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox.frameNStart = frameN  # exact frame index
        textbox.tStart = t  # local t and not account for scr refresh
        textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
        textbox.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pregunta1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pregunta1"-------
for thisComponent in pregunta1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('preg1.started', preg1.tStartRefresh)
thisExp.addData('preg1.stopped', preg1.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('textbox.text',textbox.text)
textbox.reset()
thisExp.addData('textbox.started', textbox.tStartRefresh)
thisExp.addData('textbox.stopped', textbox.tStopRefresh)
# the Routine "pregunta1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "pregunta2"-------
continueRoutine = True
# update component parameters for each repeat
text.setText('¿Conocías agunas de las letras que se mostraron en el experimento? \n\nAl finalizar apreta la barra espaciadora ')
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
button.setText('SI')
# keep track of which components have finished
pregunta2Components = [text, key_resp_5, button, button_2]
for thisComponent in pregunta2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pregunta2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pregunta2"-------
while continueRoutine:
    # get current time
    t = pregunta2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pregunta2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *button* updates
    if button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button.frameNStart = frameN  # exact frame index
        button.tStart = t  # local t and not account for scr refresh
        button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
        button.setAutoDraw(True)
    if button.status == STARTED:
        # check whether button has been pressed
        if button.isClicked:
            if not button.wasClicked:
                button.timesOn.append(button.buttonClock.getTime()) # store time of first click
                button.timesOff.append(button.buttonClock.getTime()) # store time clicked until
            else:
                button.timesOff[-1] = button.buttonClock.getTime() # update time clicked until
            if not button.wasClicked:
                continueRoutine = False  # end routine when button is clicked
                None
            button.wasClicked = True  # if button is still clicked next frame, it is not a new click
        else:
            button.wasClicked = False  # if button is clicked next frame, it is a new click
    else:
        button.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
        button.wasClicked = False  # if button is clicked next frame, it is a new click
    
    # *button_2* updates
    if button_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_2.frameNStart = frameN  # exact frame index
        button_2.tStart = t  # local t and not account for scr refresh
        button_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_2, 'tStartRefresh')  # time at next scr refresh
        button_2.setAutoDraw(True)
    if button_2.status == STARTED:
        # check whether button_2 has been pressed
        if button_2.isClicked:
            if not button_2.wasClicked:
                button_2.timesOn.append(button_2.buttonClock.getTime()) # store time of first click
                button_2.timesOff.append(button_2.buttonClock.getTime()) # store time clicked until
            else:
                button_2.timesOff[-1] = button_2.buttonClock.getTime() # update time clicked until
            if not button_2.wasClicked:
                continueRoutine = False  # end routine when button_2 is clicked
                None
            button_2.wasClicked = True  # if button_2 is still clicked next frame, it is not a new click
        else:
            button_2.wasClicked = False  # if button_2 is clicked next frame, it is a new click
    else:
        button_2.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
        button_2.wasClicked = False  # if button_2 is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pregunta2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pregunta2"-------
for thisComponent in pregunta2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('button.started', button.tStartRefresh)
thisExp.addData('button.stopped', button.tStopRefresh)
thisExp.addData('button.numClicks', button.numClicks)
if button.numClicks:
   thisExp.addData('button.timesOn', button.timesOn)
   thisExp.addData('button.timesOff', button.timesOff)
else:
   thisExp.addData('button.timesOn', "")
   thisExp.addData('button.timesOff', "")
thisExp.addData('button_2.started', button_2.tStartRefresh)
thisExp.addData('button_2.stopped', button_2.tStopRefresh)
thisExp.addData('button_2.numClicks', button_2.numClicks)
if button_2.numClicks:
   thisExp.addData('button_2.timesOn', button_2.timesOn)
   thisExp.addData('button_2.timesOff', button_2.timesOff)
else:
   thisExp.addData('button_2.timesOn', "")
   thisExp.addData('button_2.timesOff', "")
# the Routine "pregunta2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "final_2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
final_2Components = [text_2, key_resp_6]
for thisComponent in final_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
final_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "final_2"-------
while continueRoutine:
    # get current time
    t = final_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=final_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in final_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "final_2"-------
for thisComponent in final_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "final_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
