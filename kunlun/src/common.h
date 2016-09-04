/*****************************************************************************************************
 * �ļ�����common.h
 * ��  �ܣ�����ͷ�ļ���
 * ˵  �����ޡ�
*****************************************************************************************************/

#ifndef COMMON_h
#define COMMON_h

#include <stdint.h>
#DIMENSION 5

/*****************************************************************************************************
 * �ṹ����RSSI
 * ��  Ա��1.MAC ·������MAC��ַ
           2.dBm RSSI���ź�ǿ��
*****************************************************************************************************/
typedef struct{
	uint32_t x;
	uint32_t y;
	uint64_t MAC[DIMENSION];
	int16_t  dBm[DIMENSION];
}RSSI;

#endif