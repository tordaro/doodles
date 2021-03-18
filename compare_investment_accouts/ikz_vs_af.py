def ikz_utvikling(innskudd, aar, avkastning,
                  skattesats=0.3168, valutasats=0.05):
    '''
    Kalkulerer beholdning på en investringskonto zero (IKZ) gitt år,
    forventet annualisert avkastning, skattesats og mulig tap pga valuta.
    Gebyrer og andre kostnader som kommer med IKZ-konto antas å være
    neglisjerbare.

    Args:
        innskudd (float): Innskudd på starten av investeringsperioden
        aar (int): Antall år for investeringsperioden
        avkastning (float): Forventet annualisert avkastning
        skattesats (float): Skattesats på gevinst ved salg
        valutasats (float): Relativ valutaendring siden kjøp

    Returns:
        float: Netto beholdning etter endt investering
    '''
    beholdning = innskudd
    for i in range(aar):
        beholdning *= (1 + avkastning)
    beholdning *= (1 - valutasats) * (1 - skattesats)
    return beholdning


def af_utvikling(innskudd, aar, avkastning, skattesats=0.3168):
    '''
    Kalkulerer beholdning på en aksje- og fondskonto (AF) gitt år,
    forventet annualisert avkastning og skattesats. Det antas at
    valutarisiko kan unngås pga mulighet for valutakonto,
    og at hele beholdningen selges minst én gang pr år.

    Args:
        innskudd (float): Innskudd på starten av investeringsperioden
        aar (int): Antall år for investeringsperioden
        avkastning (float): Forventet annualisert avkastning
        skattesats (float): Skattesats på gevinst ved salg

    Returns:
        float: Netto beholdning etter endt investering
    '''
    beholdning = innskudd
    for i in range(aar):
        beholdning *= (1 + avkastning * (1 - skattesats))
    return beholdning


def krysning(avkastning, skattesats=0.3268, valutasats=0.05):
    '''
    Kalkulerer hvor mange år det tar før en IKZ-konto med litt
    valutarisiko lønner i forhold til en AF-konto.

    Args:
        avkastsning (float): Forventet annualisert avkastning
        valutasats (flaot): Relativ valutaendring ved salg

    Returns:
        int: Antall år før det lønner seg med IKZ
    '''
    innskudd = 100
    af_konto = 1
    ikz_konto = 0
    aar = 0
    while af_konto > ikz_konto:
        aar += 1
        af_konto = af_utvikling(innskudd, aar, avkastning, skattesats)
        ikz_konto = ikz_utvikling(innskudd, aar, avkastning,
                                  skattesats, valutasats)
    return aar


if __name__ == '__main__':
    innskudd = 100000
    skattesats = 0.3168  # I 2020 for aksjer
    valutasats = 0.05
    print(f'Mulig valutanedgang:    {valutasats:.0%}')
    print(f'Innskudd:               {innskudd}')
    avkastninger = [i/100 for i in range(10, 100, 5)]
    print('\nAvkastning     År      IKZ     AF')
    for avkastning in avkastninger:
        aar = krysning(avkastning, skattesats, valutasats)
        ikz = ikz_utvikling(innskudd, aar, avkastning, skattesats, valutasats)
        af = af_utvikling(innskudd, aar, avkastning, skattesats)
        print(f'{avkastning:.0%} {aar:>13} {ikz:>11.0f} {af:>7.0f}')
