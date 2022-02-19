# �ړ]�t�H�[�� 2005/01/06 �R��

OutError('�g�p�s�ł�') if !$MOVETOWN_ENABLE || !$TOWN_CODE;
my $townmaster=ReadTown($TOWN_CODE,'getown');
OutError('�g�p�s�ł�') if !$townmaster;

DataRead();
CheckUserPass();

OutError('�ړ]�\�ȊX��������܂���') if !$Q{towncode};
$disp.=GetMoveShopForm($Q{towncode});
OutSkin();
1;

sub GetMoveShopForm
{
	my($towncode)=@_;
	
	my($town)=ReadTown($towncode);
	return '<b>�ړ]�\�ȊX��������܂���</b>' if !$town;
	
	my $disp="";
	
	my $dist=GetTownDistance($townmaster->{position},$town->{position});
	my $movetime=GetMoveTownTime($DT,$townmaster,$town);
	
	$disp.=$TB;
	$disp.="$TR$TDB�ړ]��$TD$town->{name}$TRE";
	$disp.="$TR$TDB�R�����g$TD$town->{comment}$TRE";
	$disp.="$TR$TDB����$TD".($dist*80)."m$TRE";
	$disp.="$TR$TDB�ړ�����$TD".GetTime2HMS($movetime).' �i�\��j'.$TRE;
	$deny=0;
	
	sub GetMarkDeny
	{
		$deny=1,return " �������𖞂����Ă��܂���" if ($_[0]);
		return "";
	}
	my @flag=();
	push(@flag,"�ȑO�̈ړ]���� 10 ���ȏ�".GetMarkDeny($NOW_TIME-GetUserDataEx($DT,'_so_move_in')<864000));	#�ǉ�
	push(@flag,"���� ".GetMoneyString($town->{allowmoney})." �ȏ�".GetMarkDeny($town->{allowmoney}>$DT->{money}+$DT->{moneystock})) if $town->{allowmoney} ne '';
	push(@flag,"���� ".GetMoneyString($town->{denymoney})." �ȉ�".GetMarkDeny($town->{denymoney}<$DT->{money}+$DT->{moneystock}))  if $town->{denymoney} ne '';
	push(@flag,"�M���h ".join("/",map{GetTagImgGuild($_,1,1)}split(/\W/,$town->{allowguild})).($town->{onlyguild} ? '':' ����уM���h������')." �̂�".GetMarkDeny($DT->{guild} ne '' && !scalar(grep($_ eq $DT->{guild},split(/[^\w]+/,$town->{allowguild}))))) if $town->{allowguild} ne '';
	push(@flag,"�M���h ".join("/",map{GetTagImgGuild($_,1,1)}split(/\W/,$town->{denyguild})).($town->{onlyguild} ? ' ����уM���h������':'')." �ȊO".GetMarkDeny($DT->{guild} ne '' && scalar(grep($_ eq $DT->{guild},split(/[^\w]+/,$town->{denyguild}))))) if $town->{denyguild} ne '';
	push(@flag,"�g�b�v�l���� $town->{allowtopcount} ��ȏ�".GetMarkDeny($town->{allowtopcount}>$DT->{rankingcount})) if $town->{allowtopcount} ne '';
	push(@flag,"�g�b�v�l���� $town->{denytopcount} ��ȉ�".GetMarkDeny($town->{denytopcount}<$DT->{rankingcount}))  if $town->{denytopcount} ne '';
	push(@flag,"�J�Ɗ��� ".GetTime2HMS($town->{allowfoundation})." �ȏ�".GetMarkDeny($town->{allowfoundation}>$NOW_TIME-$DT->{foundation})) if $town->{allowfoundation} ne '';
	push(@flag,"�J�Ɗ��� ".GetTime2HMS($town->{denyfoundation})." �ȉ�".GetMarkDeny($town->{denyfoundation}<$NOW_TIME-$DT->{foundation}))  if $town->{denyfoundation} ne '';
	push(@flag,"�M���h�����̂� ".GetMarkDeny($DT->{guild} eq '')) if $town->{onlyguild} ne '';
	push(@flag,"�M���h�������̂� ".GetMarkDeny($DT->{guild} ne '')) if $town->{noguild} ne '';
	push(@flag,"�E�� ".join("/",map{$JOBTYPE{$_}}split(/\W+/,$town->{allowjob})).($town->{onlyjob} ? '':' ����ѐE�ƕs��')." �̂�".GetMarkDeny($DT->{job} ne '' && !scalar(grep($_ eq $DT->{job},split(/\W+/,$town->{allowjob}))))) if $town->{allowjob} ne '';
	push(@flag,"�E�� ".join("/",map{$JOBTYPE{$_}}split(/\W+/,$town->{denyjob})).($town->{onlyjob} ? ' ����ѐE�ƕs��':'')." �ȊO".GetMarkDeny($DT->{job} ne '' && scalar(grep($_ eq $DT->{job},split(/\W+/,$town->{denyjob}))))) if $town->{denyjob} ne '';
	push(@flag,"�E�ƓX�܂̂� ".GetMarkDeny($DT->{job} eq '')) if $town->{onlyjob} ne '';
	push(@flag,"�E�ƕs��X�܂̂� ".GetMarkDeny($DT->{job} ne '')) if $town->{nojob} ne '';
	$disp.="$TR$TDB�ړ]����$TD�E".join("<br>�E",@flag)."$TRE" if scalar(@flag);
	$disp.=$TBE;
	
	return $disp if $deny;
	$disp.=<<"HTML";
		<hr width=500 noshade size=1>
		<form action="action.cgi" $METHOD>
		<input type=hidden name=key value="move-s">
		$USERPASSFORM
		<input type=hidden name=towncode value="$towncode">
		$TB$TR
		$TDB�ړ]��ł̖��O(ID)$TD<input type=text name=name value="$DT->{name}">(���p�S�pOK)$TRE
		$TR$TDB���݂̃p�X���[�h$TD<input type=password name=pass value="">$TRE$TBE
		<br><input type=submit value="�ړ]�葱�J�n">
		</form>
		<hr width=500 noshade size=1>
		<table><tr><td>�ړ]�ň����p����Ȃ��f�[�^�͉��L�̒ʂ�ł��B����ȊO�͂قڂ��̂܂܈����p����܂��B
		<ul>
		<li>�O���̏��ʏ��
		<li>�͂��Ă����莆�i�S�Ĕj���j
		</ul>
		�ȉ��̏ꍇ�͈ړ]�̍ۓX�܃f�[�^���ꕔ�����܂��B
		<ul>
		<li>�V�X�e���������œX�܃f�[�^�Ɍ݊������Ȃ��ꍇ
		</ul>
		�ȉ��̏ꍇ�͈ړ]�ł��܂���B
		<ul>
		<li>�ړ]�悪�����̏ꍇ
		<li>�ړ]��ɓ������O(ID)��X�ܖ�������ꍇ
		</ul></td></tr></table>
HTML
	return $disp;
}

