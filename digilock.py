��
͋HPc           @   s�   d  Z  d d k Z d d k Z d d k Z d d k Z d a d a d a d �  Z d �  Z	 d �  Z
 d d	 � Z d d
 � Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d GHd S(   s5   
Created on Tue Aug 21 18:07:36 2012

@author: bernd
i����Ns   10.155.59.248ia�  i   c   	   	   C   sw  t  i |  | f � } | i | t d � t d � � t i d � y	t | d � } | i | d t | � d !d d t | � � t | � d } | i t d � | t | � � } | | d | !} d | j o+ | d t | � d !} t	 | � d } nE d	 | j o+ | d t | � d !} t	 | � d
 } n t	 | � } | i
 �  Wn$ | i
 �  d Gt i �  d GHn X| S(   s<   Send simple query to Digilock and return the requested valuei   i
   g�������?i   i    t   =t   mg����MbP?t   ug�����ư>s   Unexpected error:(   t   sockett   create_connectiont   sendallt   chrt   timet   sleept   recv_timeout2t   findt   lent   floatt   closet   syst   exc_info(	   t   ipt   portt   commandt   st   answert   indexit   indexet	   answercutt   value(    (    s   digilock.pyt   simplequery   s(    !>!
c         C   sD   t  i |  | f � } | i | t d � t d � � | i �  d  S(   Ni   i
   (   R   R   R   R   R   (   R   R   R   R   (    (    s   digilock.pyt   simplecommand+   s    !c      	   C   s�   t  i |  | f � } | i | t d � t d � � t i d � yr t | d � } | i | d t | � d !d d t | � � t | � d } | | d t | � !} | i	 �  Wn$ | i	 �  d Gt
 i �  d GHn X| S(   Ni   i
   g�������?i   i    R    s   Unexpected error:(   R   R   R   R   R   R   t   recv_timeoutR
   R   R   R   R   (   R   R   R   R   R   R   R   (    (    s   digilock.pyt	   longquery/   s    !>
c         C   s�   |  i  d � g  } d } t i �  } x� | o t i �  | | j o Pn! t i �  | | d j o Pn yD |  i d � } | o | i | � t i �  } n t i d � Wq( q( Xq( t d i | � � } | GH| S(   Ni    t    i
   i    g�������?(   t   setblockingR   t   recvt   appendR   t   strt   join(   t
   the_sockett   timeoutt
   total_datat   datat   begin(    (    s   digilock.pyR   A   s(      c         C   s�   |  i  d � g  } d } t i �  } x} | o Pn! t i �  | | d j o Pn yD |  i d � } | o | i | � t i �  } n t i d � Wq( q( Xq( t d i | � � } | S(   Ni    R   i
   i    g�������?(   R   R   R   R    R   R!   R"   (   R#   R$   R%   R&   R'   (    (    s   digilock.pyR	   _   s&      c          C   s*   d t  t � d }  t t t |  � } | S(   Ns   scope:chs   :mean?(   R!   t	   piezochanR   R   R   (   R   R   (    (    s   digilock.pyt   getoutputvoltage}   s    c         C   s$   d t  |  � } t t t | � d  S(   Ns   offset:value=(   R!   R   R   R   (   t   offsetvoltageR   (    (    s   digilock.pyt	   setoffset�   s    c          C   s   d }  t  t t |  � S(   Ns   offset:value?(   R   R   R   (   R   (    (    s   digilock.pyt	   getoffset�   s    c         C   s$   d t  |  � } t t t | � d  S(   Ns   scan:amplitude=(   R!   R   R   R   (   t   amplR   (    (    s   digilock.pyt   setscanrange�   s    c         C   s$   d t  |  � } t t t | � d  S(   Ns   scan:frequency=(   R!   R   R   R   (   t   freqR   (    (    s   digilock.pyt   setscanfrequency�   s    c         C   s$   d t  |  � } t t t | � d  S(   Ns   scope:smooth:number=(   R!   R   R   R   (   t   pointsR   (    (    s   digilock.pyt   setaveraging�   s    c         C   s$   d t  |  � } t t t | � d  S(   Ns   scope:timescale=(   R!   R   R   R   (   R   R   (    (    s   digilock.pyt   setscopetimescale�   s    c         C   s=   |  o
 d } n |  t  j o
 d } n d GHt t t | � S(   Ns   scan:enable=trues   scan:enable=falses   boolean needed(   t   FalseR   R   R   (   t   boolR   (    (    s   digilock.pyt
   switchscan�   s    

c          C   s�   d }  t  t t |  � } d GH| i t d � t d � � } | GHt t | � } | d =g  } | D] } | t t | � qb ~ } t | �  } | GH| S(   Ns   scope:graph?s   this is the getscopedataoutputi   i
   i����(	   R   R   R   t   splitR   t   mapt   ssplitR   t   zip(   R   t
   scope_datat   scope_data_listt   scope_data_splittedt   _[1]t   xt   scope_data_splitted_floatt   scope_data_transposed(    (    s   digilock.pyt   getscopedata�   s    *c         C   s   |  i  t d � � S(   Ni	   (   R7   R   (   t   string_to_split(    (    s   digilock.pyR9   �   s    t   test(   t   __doc__R   t   reR   R   R   R   R(   R   R   R   R   R	   R)   R+   R,   R.   R0   R2   R3   R6   RB   R9   (    (    (    s   digilock.pyt   <module>   s.   													