# �g�їp���j���[ 2004/01/20 �R��

$NOITEM=1;
DataRead();
CheckUserPass(1);

$disp.=$HTML_TITLE.'<A HREF="index.cgi" TARGET=_top>[�g�b�v]</A> ';
my $now=$DTlasttime+$TZ_JST-$DATE_REVISE_TIME;
my $nextday=$now+$ONE_DAY_TIME-($now % $ONE_DAY_TIME);
$disp.='[���񌈎Z '.GetTime2FormatTime($nextday-$TZ_JST+$DATE_REVISE_TIME).' �܂ł���'.GetTime2HMS(int(($nextday-$now)/60)*60+59).']<br>';

$disp.=GetMenuTag('shop-m',	'[�s��]');
$disp.=GetMenuTag('log',		'[�V��]');

$disp.='<hr width=500 noshade size=1>';
if($USER && $USER ne 'soldoutadmin')
{
	$disp.=GetMenuTag('main',		'[�X����]');
	$disp.=GetMenuTag('stock',		'[�q��]');
	$disp.=GetMenuTag('sc',		'[��I]');
	$disp.=GetMenuTag('sweep',		'[���|��]');
}

OutSkin();
1;
