# �˗��t�H�[�� 2005/03/30 �R��

DataRead();
CheckUserPass();
RequireFile('inc-req.cgi');
RequireFile('inc-html-ownerinfo.cgi');

$disp.="<BIG>���˗���</BIG><br><br>";

ReqSet();
my $limit=GetTime2HMS($REQUEST_LIMIT);
$disp.=<<STR;
$TB$TR$TD
$AucImg
�V�����˗����������񂾂ȁH ����Ȃ璍�ӎ������悭�ǂ�ł���B<br>
�E�˗��͓����� <b>$REQUEST_CAPACITY��</b>�������邱�Ƃ��ł��܂���B<br>
�E�˗����B�����ꂽ��<SPAN>���ɗ��Ă�������</SPAN>�B<br>
�E�L������ <b> $limit</b>�ȓ��Ɏ��ɗ��Ȃ��ƈ˗��͔j������܂��B<br>
�E�̔�/����ł͉��i�� <b>$DTTaxrate%</b>�̐ŋ����˗��҂ɂ�����܂��B
$TRE$TBE
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="req-s">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="new">
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<BIG>�������^�C�v</BIG>�F�˗��i <SELECT NAME=prn SIZE=1>
$formlist
</SELECT> �𐔗� <INPUT TYPE=TEXT NAME=pr SIZE=7> �����ė��Ă��ꂽ���ɂ�<br>
���� <SELECT NAME=it SIZE=1>
$formitem
</SELECT> �𐔗� <INPUT TYPE=TEXT NAME=num SIZE=7> �����グ�܂��B
<INPUT TYPE=SUBMIT VALUE='�쐬'>
</FORM>
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="req-s">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="new">
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<BIG>���̔��^�C�v</BIG>�F�̔��i <SELECT NAME=it SIZE=1>
$formitem
</SELECT> �𐔗� <INPUT TYPE=TEXT NAME=num SIZE=7> ����o���̂�<br>
���i <INPUT TYPE=TEXT NAME=pr SIZE=7> $term[2](
<INPUT TYPE=CHECKBOX NAME=unit>�P���w��)�Ŕ����Ă��������B
<INPUT TYPE=HIDDEN NAME=prn VALUE="-1">
<INPUT TYPE=SUBMIT VALUE='�쐬'>
</FORM>
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="req-s">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="new">
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<BIG>������^�C�v</BIG>�F�˗��i <SELECT NAME=prn SIZE=1>
$formlist
</SELECT> �𐔗� <INPUT TYPE=TEXT NAME=pr SIZE=7> �����ė��Ă��ꂽ���ɂ�<br>
���i <INPUT TYPE=TEXT NAME=num SIZE=7> $term[2](
<INPUT TYPE=HIDDEN NAME=it VALUE="-1">
<INPUT TYPE=CHECKBOX NAME=unit>�P���w��)�Ŕ������܂��B
<INPUT TYPE=SUBMIT VALUE='�쐬'>
</FORM>
STR
OutSkin();
1;


sub ReqSet
{
	my @sort;
	foreach(1..$MAX_ITEM){$sort[$_]=$ITEM[$_]->{sort}};
	my @itemlist=sort { $sort[$a] <=> $sort[$b] } (1..$MAX_ITEM);
	$formitem="";
	$formlist="";		#�S�̂̃��X�g
	foreach my $idx (@itemlist)
	{
		next if !$ITEM[$idx]->{name};
		next if $ITEM[$idx]->{flag}=~/r/;	# r �˗��s��
		my $cnt=$DT->{item}[$idx-1];
		my $scale=$ITEM[$idx]->{scale};
		my $price=$ITEM[$idx]->{price};
		$formlist.="<OPTION VALUE=\"$idx\">$ITEM[$idx]->{name}(@".GetMoneyString($price).")" if $ITEM[$idx]->{flag}!~/o/;		# o �˗��͏o�i�̂�
		$formitem.="<OPTION VALUE=\"$idx\">$ITEM[$idx]->{name}($cnt$scale@".GetMoneyString($price).")" if $cnt;
	}
}

