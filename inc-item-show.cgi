# �A�C�e���񉺐��� 2004/01/20 �R��

$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="sc-s">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=bk VALUE="$Q{bk}">
<INPUT TYPE=HIDDEN NAME=item VALUE="$itemno">
<BIG>����F</BIG>
<SELECT NAME=no>
STR
foreach my $cnt (1..$DT->{showcasecount})
{
	$disp.="<OPTION VALUE='".($cnt-1)."'".($showcase==$cnt?' SELECTED':'').">";
	$disp.="�I$cnt($ITEM[$DT->{showcase}[$cnt-1]]->{name})";
}
	$disp.="</SELECT>";
	$disp.="�֕W�����i��";
	$disp.=<<STR;
<SELECT NAME=per>
<OPTION VALUE='50'>5����
<OPTION VALUE='60'>4����
<OPTION VALUE='70'>3����
<OPTION VALUE='80'>2����
<OPTION VALUE='90'>1����
<OPTION VALUE='100' SELECTED>�܂�
<OPTION VALUE='110'>1����
<OPTION VALUE='120'>2����
</SELECT>
�܂���
<INPUT TYPE=TEXT NAME=prc SIZE=6 VALUE="$Q{pr}">�~
��
<INPUT TYPE=SUBMIT VALUE='�񂷂�'>
(����${\GetTime2HMS($TIME_EDIT_SHOWCASE)}����)
</FORM>
STR
1;
