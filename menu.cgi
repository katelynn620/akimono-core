use utf8;
# 携帯用メニュー 2004/01/20 由來

$NOITEM=1;
DataRead();
CheckUserPass(1);

$disp.=$HTML_TITLE.'<A HREF="index.cgi" TARGET=_top>[トップ]</A> ';
my $now=$DTlasttime+$TZ_JST-$DATE_REVISE_TIME;
my $nextday=$now+$ONE_DAY_TIME-($now % $ONE_DAY_TIME);
$disp.='['.l('次回決算 %1 まであと%2',GetTime2FormatTime($nextday-$TZ_JST+$DATE_REVISE_TIME),GetTime2HMS(int(($nextday-$now)/60)*60+59)).']<br>';

$disp.=GetMenuTag('shop-m',	'['.l('市場').']');
$disp.=GetMenuTag('log',		'['.l('新聞').']');

$disp.='<hr width=500 noshade size=1>';
if($USER && $USER ne 'soldoutadmin')
{
	$disp.=GetMenuTag('main',		'['.l('店長室').']');
	$disp.=GetMenuTag('stock',		'['.l('倉庫').']');
	$disp.=GetMenuTag('sc',		'['.l('陳列棚').']');
	$disp.=GetMenuTag('sweep',		'['.l('お掃除').']');
}

OutSkin();
1;
