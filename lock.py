Ñò
ÏHPc           @   s7   d  Z  d d k Z d d k Z d d  Z d   Z d S(   s5   
Created on Wed Aug 22 12:49:03 2012

@author: bernd
iÿÿÿÿNi
   c         C   s¹   t  i   } | g d } x t o t i d  t  i   } | i |  t |  |  j o | d =n t |  } t  i	 |  t i d  t  i   t
 |  d t
 |  GHq Wd S(   s¥   force the voltage offset (center of allowed SCC output
    volltage window) to follow the laserdrift averaging over
    the last num_averages measurements.
    
    i
   g      à?i   gÉ?s   ; N(   t   digilockt	   getoffsett   Truet   timet   sleept   getoutputvoltaget   appendt   lent   meant	   setoffsett   str(   t   num_averagest   initial_offsett   offsetst   measurement_valuet   offset(    (    s   lock.pyt   lock   s    
 
c         C   sY   t  |   d j o t d  Sg  } |  D] } | t |  q) ~ } t |  t  |   S(   s%   return mean of list given as argumenti    t   nan(   R   t   floatt   sum(   t
   numberListt   _[1]t   xt	   floatNums(    (    s   lock.pyR   '   s    '(   t   __doc__R    R   R   R   (    (    (    s   lock.pyt   <module>   s   