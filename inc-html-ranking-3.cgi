# ���܃��X�g�\�� 2005/01/06 �R��

$disp.="<BIG>���V���F���܃��X�g</BIG><br><br>";
$disp.=$TB.$TR;

	@DT=sort{$b->{rankingcount}<=>$a->{rankingcount}}@DT;

$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT[0]->{name},$DT[0]->{icon});
$disp.=$TD."<SPAN>�ő��D��</SPAN><br><b>".$DT[0]->{shopname}."</b>";
$disp.="<td>�D����<br>".($DT[0]->{rankingcount}+0)."��";
$disp.="<td>".$DT[0]->{comment};

	@DT=sort{$b->{taxyesterday}<=>$a->{taxyesterday}}@DT;

$disp.=$TRE.$TR;
$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT[0]->{name},$DT[0]->{icon});
$disp.=$TD."<SPAN>�[�Ńg�b�v</SPAN><br><b>".$DT[0]->{shopname}."</b>";
$disp.="<td>�O���[�ŋ�<br>".GetMoneyString($DT[0]->{taxyesterday});
$disp.="<td>".$DT[0]->{comment};

	@DT=sort{$b->{money}<=>$a->{money}}@DT;

$disp.=$TRE.$TR;
$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT[0]->{name},$DT[0]->{icon});
$disp.=$TD."<SPAN>��x��</SPAN><br><b>".$DT[0]->{shopname}."</b>";
$disp.="<td>����<br>".GetMoneyString($DT[0]->{money});
$disp.="<td>".$DT[0]->{comment};

	@DT=reverse(@DT);

$disp.=$TRE.$TR;
$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT[0]->{name},$DT[0]->{icon});
$disp.=$TD."<SPAN>�n�R�q�}�Ȃ�</SPAN><br><b>".$DT[0]->{shopname}."</b>";
$disp.="<td>����<br>".GetMoneyString($DT[0]->{money});
$disp.="<td>".$DT[0]->{comment};

	@DT=sort{$b->{costyesterday}<=>$a->{costyesterday}}@DT;

$disp.=$TRE.$TR;
$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT[0]->{name},$DT[0]->{icon});
$disp.=$TD."<SPAN>�ێ�����肷��</SPAN><br><b>".$DT[0]->{shopname}."</b>";
$disp.="<td>�O���ێ���<br>".GetMoneyString($DT[0]->{costyesterday});
$disp.="<td>".$DT[0]->{comment};

	@DT=sort{$b->{trush}<=>$a->{trush}}@DT;

$disp.=$TRE.$TR;
$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT[0]->{name},$DT[0]->{icon});
$disp.=$TD."<SPAN>�|���T�{�肷��</SPAN><br><b>".$DT[0]->{shopname}."</b>";
$disp.="<td>����<br>".GetCleanMessage($DT[0]->{trush});
$disp.="<td>".$DT[0]->{comment};

	@DT=sort{$b->{rank}<=>$a->{rank}}@DT;

$disp.=$TRE.$TR;
$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT[0]->{name},$DT[0]->{icon});
$disp.=$TD."<SPAN>�������ܑ�l�C</SPAN><br><b>".$DT[0]->{shopname}."</b>";
$disp.="<td>�l�C<br>".GetRankMessage($DT[0]->{rank});
$disp.="<td>".$DT[0]->{comment};

	@DT=reverse(@DT);

$disp.=$TRE.$TR;
$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT[0]->{name},$DT[0]->{icon});
$disp.=$TD."<SPAN>���q���񗈂Ă�</SPAN><br><b>".$DT[0]->{shopname}."</b>";
$disp.="<td>�l�C<br>".GetRankMessage($DT[0]->{rank});
$disp.="<td>".$DT[0]->{comment};

$disp.="</td></tr></table>";
1;
