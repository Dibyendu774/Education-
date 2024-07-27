
$iNb  : 7;
$iTimer : 25;
/* En ré&alité des demi-pauses */
$iPause : 1;

#slideshow-sw {
  position: relative;
  width: 640px;
  height: 310px;
  padding: 15px;
  margin: 5% auto 2em;
  border: 1px solid #ddd;
  background-color: #FFF;
  background: linear-gradient(#FFF, #FFF 20%, #EEE 80%, #DDD);
  border-radius: 2px 2px 2px 2px;
  /*box-shadow: 0 0 3px rgba(0,0,0, 0.2);*/
}

#slideshow-sw:before,
#slideshow-sw:after {
  position: absolute;
  bottom: 16px;
  z-index: -10;
  width: 50%;
  height: 20px;
  content: " ";
  background: rgba(0,0,0,0.1);
  border-radius: 50%;
  /*box-shadow: 0 0 3px rgba(0,0,0, 0.4), 0 20px 10px rgba(0,0,0, 0.7);*/
}

#slideshow-sw:before {
  left: 0;
  transform: rotate(-4deg)
}

#slidehow-sw:after {
  right: 0;
  transform: rotate(4deg);
}

/* gestion des dimensions et débordement du conteneur */
#slideshow-sw .container {
  position:relative;
  width: 640px;
  height: 309px;
  overflow: hidden;
  font-size:0px;

}

/* on prévoit un petit espace gris pour la timeline */
#slideshow-sw .container:after {
  position:absolute;
  bottom: 0; left:0;
  content: " ";
  width: 100%;
  height: 1px;
  background: #999;
}
/* 
le conteneur des slides
en largeur il fait 100% x le nombre de slides
*/
#slideshow-sw .slider-sw {
  position: absolute;
  left:0; top:0;
  width: #{($iNb ) * 100%};
  height: 310px; 
}

/* annulation des marges sur figure */
#slideshow-sw figure {
  position:relative;
  display:inline-block;
  padding:0; margin:0;
}

/* effets vignette sur les images */
#slideshow-sw figure:after {

  display:block;
  content: " ";
  top:0; left:0;
  width: 100%; height: 100%;
  /*box-shadow: 0 0 65px rgba(0,0,0, 0.5) inset;*/
}


/* styles des légendes */
#slideshow-sw figcaption {
  position:absolute;
  left:0; right:0; bottom: 5px;
  padding: 7px;
  margin:0;
  border-top: 1px solid rgb(225,225,225);
  text-align:center;
  letter-spacing: 0.05em;
  word-spacing: 0.05em;
  font-family: Georgia, Times, serif;
  background: #fff;
  background: rgba(255,255,255,0.7);
  color: #555;
  text-shadow: -1px -1px 0 rgba(255,255,255,0.3);
}

/* Durée total - ( nombre de pause total ) - (nombre de pause total poins 2 )*/
$iTimerPause :  ($iPause * $iNb) +  ($iPause * ($iNb - 2)) ;
$iTimerTransition :  ($iTimer - $iTimerPause) ;
$iTransitionPourcentage :  ($iTimerTransition / ($iNb - 1)) * 100 /  $iTimer ;
$iPausenPourcentage : $iPause * 100 /  $iTimer ;
/*
 
iTimerMoinsPause  = #{$iTimerPause }
iTimerTransition  = #{$iTimerTransition } 
                  = #{$iTimerPause + $iTimerTransition}
 
une total pause %       =  #{($iPausenPourcentage * $iNb) +  ($iPausenPourcentage * ($iNb - 2))}
une total deplacement % = #{$iTransitionPourcentage * ($iNb - 1)}  
                        =  #{$iTransitionPourcentage * ($iNb - 1)  + ($iPausenPourcentage * $iNb) +  ($iPausenPourcentage * ($iNb - 2))} 
*/

/*
iPausenPourcentage      = #{$iPausenPourcentage}
iTransitionPourcentage  = #{$iTransitionPourcentage }
*/
$iQt : 100 / 7;
$iCount : 0 ;
$i : 0;
@keyframes slider-sw {
  @for $i from 0 through $iNb - 1{
    #{$iCount}% {left: #{-100% * $i };/*Start*/}
    $iAdd : $iCount;
    @if ( $i < 1 ){
      #{$iAdd +  $iPausenPourcentage}% {left: #{-100% * $i };}
      $iAdd : $iAdd + $iPausenPourcentage +  $iTransitionPourcentage;
    } @else { 
      $iMore : $iAdd + $iPausenPourcentage + $iPausenPourcentage ;
      @if ( $iMore > 100) {
        #{$iAdd +  $iPausenPourcentage}% {left: #{-100% * $i };}
         $iAdd : $iAdd + $iPausenPourcentage +  $iTransitionPourcentage;
      } @else {
        #{$iMore}% {left: #{-100% * $i };}
         $iAdd : $iAdd + $iPausenPourcentage + $iPausenPourcentage + $iTransitionPourcentage;
      }
    } 
    $iCount :  $iAdd ; 
   
  }
}


#slideshow-sw .slider-sw {
  animation-name : slider-sw;
  animation-direction : alternate;
  animation-fill-mode : none ;
  animation-duration :#{$iTimer}s;
  animation-iteration-count : infinite;
  animation-timing-function : ease-in-out;
  animation-delay : #{$iPause}s;
}