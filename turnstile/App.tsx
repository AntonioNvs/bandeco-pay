import React, { useEffect, useState } from 'react';
import { Image, View, Text, StyleSheet, ActivityIndicator } from 'react-native';
import NfcManager, { NfcTech } from 'react-native-nfc-manager';

NfcManager.start();

const App = () => {
  const [nfcTag, setNfcTag] = useState(null);
  const [loading, setLoading] = useState(true);
  const [isNfcActive, setIsNfcActive] = useState(false);

  const raphinhaId = "64090D64"
  const bernardoId = "8E87EE9C"
  const antonioId = "7CA288BD"

  // Função para iniciar a leitura NFC
  const startNfcReading = async () => {
    try {
      await NfcManager.cancelTechnologyRequest().catch(() => {});

      await NfcManager.requestTechnology(NfcTech.Ndef);
      const tag = await NfcManager.getTag();
      setNfcTag(tag);
      setLoading(false); // Finaliza o loading
      setIsNfcActive(true);
      console.log(tag)
      // Aguarda 5 segundos e volta para a tela de leitura
      setTimeout(() => {
        setNfcTag(null); // Reseta os dados da tag
        setLoading(true); // Volta para o estado de loading
        startNfcReading();
      }, 6000); // 5 segundos

    } catch (ex) {
      console.warn(ex);
    } finally {
      if (isNfcActive) {
        NfcManager.cancelTechnologyRequest();
        setIsNfcActive(false);
      }
    }
  };

  useEffect(() => {
    // Ativa a leitura de NFC automaticamente ao carregar a tela
    startNfcReading();

    // Limpa o listener de NFC ao desmontar o componente
    return () => {
      NfcManager.setEventListener(NfcTech.Ndef, null);
    };
  }, []);

  if (loading) {
    return (
      <View style={styles.containerWaiting}>
        <Text style={styles.title}>Aproxime o cartão de identificação</Text>
        <ActivityIndicator size="large" color="#ffffff" />
      </View>
    );
  }

  return (
    <View style={[
        styles.containerPersonalData,
        nfcTag?.id == raphinhaId ? {backgroundColor: "#e52e4d"} : {backgroundColor: "#33cc95"}
      ]}>
      <Image 
        style={styles.img}
        source={nfcTag?.id == raphinhaId ? require("./assets/error.png") : require("./assets/check_circle.png")}></Image>        
      <Text style={styles.titlePersonalData}>{nfcTag?.id == raphinhaId ? "SALDO INDISPONÍVEL" : "TRANSAÇÃO OCORRIDA"}</Text>
      <Text style={styles.textSubtype}>{nfcTag?.id == raphinhaId ? "RAPHAEL AROLDO CARREIRO MENDES" : "ANTÔNIO CAETANO NEVES NETO"}</Text>
      <Text style={styles.textSubtype}>
        SALDO USADO: <Text style={styles.textData}>R$ 5,60</Text>
      </Text>
      <Text style={styles.textSubtype}>
        SALDO RESTANTE: <Text style={styles.textData}>{nfcTag?.id == raphinhaId ? "R$ 1,70" : "R$ 45,60"}</Text>
      </Text>
    </View>
  );
};

const styles = StyleSheet.create({
  containerWaiting: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#e52e4d',
  },
  containerPersonalData: {
    flex: 1,
    justifyContent: 'center',
    backgroundColor: '#33cc95',
    padding: 24
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    marginBottom: 20,
    color: '#f0f0f0',
    marginHorizontal: 40,
    textAlign: "center",
    lineHeight: 48,
  },
  card: {
    width: '90%',
    padding: 12,
    backgroundColor: '#fff',
    borderRadius: 10,
    elevation: 4,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.3,
    shadowRadius: 4,
    alignItems: 'center',
  },
  textSubtype: {
    fontSize: 24,
    marginBottom: 20,
    color: "#f0f0f0",
    textAlign: "left",
    fontWeight: "bold"
  },
  textData: {
    fontSize: 24,
    color: "#f0f0f0",
    textAlign: "left",
    
  },
  titlePersonalData: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 32,
    color: '#f0f0f0',
    textAlign: "left",
    lineHeight: 40,
  },
  img: {
    width: 256,
    height: 256,
    alignSelf: "center"
  }
});

export default App;