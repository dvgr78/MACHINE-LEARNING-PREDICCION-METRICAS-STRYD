-- **********************************************************************************************
-- En esta tabla se extraerán los datos del archivo SEGMENTOS.txt com tabla de aterrizaje,
-- asignaremos a cada campo su tipo correspondiente haciendo mediante PwC las tranformaciones
-- correspondientes.
-- Ojo Eliminaremos RFP para calcularlo después con más decimales
-- **********************************************************************************************

CREATE TABLE [dbo].[STG_SEGMENTOS_TIPOOK](
	[FECHA]				[date]				NULL,
	[CONTADOR]			[int]				NULL,
	[CP]				[int]				NULL,
	[ID_TERRENO]		[int]				NULL,
	[ID_TIPOE]			[int]				NULL,
	[SEGMENTO]			[int]				NULL,
	[DURACION]			[int]				NULL,
	[DISTANCIA]			[int]				NULL,
	[POTENCIA]			[int]				NULL,
	[RITMO]				[int]				NULL,
	[FREC_CARDIACA]		[int]				NULL,
	[CADENCIA]			[int]				NULL,
	[FP]				[int]				NULL,
	[TSC]				[int]				NULL,
	[LSS]				[decimal](15, 3)	NULL,
	[OSC_VERTICAL]		[decimal](15, 3)	NULL,
	[AIRE]				[int]				NULL,
	[L_ZANCADA]			[decimal](15, 3)	NULL,
	[PENDIENTE]			[decimal](15, 3)	NULL,
	[ALTITUD]			[int]				NULL,
	[RSS]				[int]				NULL,
	[DESNIVEL]			[int]				NULL
) ON [PRIMARY]