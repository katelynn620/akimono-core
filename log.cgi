# �V�� 2004/01/20 �R��

$NOITEM=1 if ($Q{t}==1);
DataRead();
CheckUserPass(1);

$disp.=GetMenuTag('log',	'[����]')
	.GetMenuTag('log',	'[����]','&t=3')
	.GetMenuTag('log',	'[����]','&t=4')
	.GetMenuTag('log',	'[�݈�]','&t=5');
$disp.="<hr width=500 noshade size=1>";

if ($Q{t}==5) {
RequireFile('inc-html-ranking-2.cgi');
} elsif ($Q{t}==4) {
RequireFile('inc-html-ranking.cgi');
} elsif ($Q{t}==3) {
RequireFile('inc-html-ranking-3.cgi');
} else {
ReadLog($DT->{id},$Q{lmd}+0,$Q{kw},$Q{tgt});
RequireFile('inc-html-log.cgi');
}

OutSkin();
1;
