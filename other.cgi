# �e��葱 2005/01/06 �R��

DataRead();
CheckUserPass();
RequireFile('inc-html-ownerinfo.cgi');

$disp.="<BIG>���e��葱</BIG><br><br>";

$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE=user>
<INPUT TYPE=HIDDEN NAME=mode VALUE=comment>
$USERPASSFORM
<SPAN>�R�����g</SPAN>
<INPUT TYPE=TEXT NAME=cmt SIZE=36 VALUE="$DT->{comment}">
<INPUT TYPE=SUBMIT VALUE="�ύX����">
</FORM>
STR

$i_rand=int(rand($ICON_NUMBER))+1;
$disp.=<<STR;
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE=user>
<INPUT TYPE=HIDDEN NAME=mode VALUE=icon>
$USERPASSFORM
<SPAN>�X���A�C�R���ύX</SPAN>�F
<input type="button" value="�A�C�R���ꗗ" onclick="javascript:window.open('action.cgi?key=icon','_blank','width=450,height=380,scrollbars')">
<SELECT NAME=icon>
<OPTION value="$i_rand" selected>�����_��</OPTION>
STR

foreach my $i(1..$ICON_NUMBER)
	{
	$disp.=qq|<OPTION value="$i">�摜$i</OPTION>|;
	}

$disp.=<<"STR";
</SELECT> 
<INPUT TYPE=SUBMIT VALUE="�ύX����">
</FORM>
STR

$disp.=<<STR;
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE=user>
<INPUT TYPE=HIDDEN NAME=mode VALUE=shopname>
$USERPASSFORM
<SPAN>�X�ܖ��ύX</SPAN>(������p$term[0]50,000$term[1])
<INPUT TYPE=TEXT NAME=rename SIZE=30 VALUE="">
<INPUT TYPE=SUBMIT VALUE="��������">
</FORM>
STR

$disp.=<<STR;
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE=user>
<INPUT TYPE=HIDDEN NAME=mode VALUE=owname>
$USERPASSFORM
<SPAN>�X�����ύX</SPAN>(������p$term[0]50,000$term[1])
<INPUT TYPE=TEXT NAME=owname SIZE=20 VALUE="">
<INPUT TYPE=SUBMIT VALUE="��������">
</FORM>
STR

$disp.=<<STR;
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE=user>
<INPUT TYPE=HIDDEN NAME=mode VALUE=repass>
$USERPASSFORM
<SPAN>�p�X���[�h�ύX</SPAN> �F 
<INPUT TYPE=TEXT NAME=pw1 SIZE=10 maxlength=12 VALUE="">�V�p�X 
<INPUT TYPE=TEXT NAME=pw2 SIZE=10 maxlength=12 VALUE="">�V�p�X�ē��� 
<INPUT TYPE=SUBMIT VALUE="�ύX����">
</FORM>
STR


if ( ($NOW_TIME-$DT->{foundation}) > 3600*3 ) {
$disp.=<<STR;
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE=user>
<INPUT TYPE=HIDDEN NAME=mode VALUE=restart>
$USERPASSFORM
<BIG>���ďo��(��蒼��)</BIG> �F 
<INPUT TYPE=TEXT NAME=rss SIZE=10 maxlength=12 VALUE="">�m�F�̂��� restart �Ɠ��� 
<INPUT TYPE=SUBMIT VALUE="��蒼��">
</FORM>
STR
} else {
$disp.=<<STR;
<hr width=500 noshade size=1>
<BIG>���ďo��(��蒼��)</BIG> �F 
<b>�n�ƌ�3���Ԉȓ��͍ďo���ł��܂���</b>
STR
}

$disp.=<<STR;
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE=user>
<INPUT TYPE=HIDDEN NAME=mode VALUE=cls>
$USERPASSFORM
<BIG>���X(�ēo�^�s��)</BIG> �F 
<INPUT TYPE=TEXT NAME=cls SIZE=10 maxlength=12 VALUE="">�m�F�̂��� closeshop �Ɠ��� 
<INPUT TYPE=SUBMIT VALUE="�X���܂�">
</FORM>
STR

OutSkin();
1;
