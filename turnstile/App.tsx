import { StatusBar } from 'expo-status-bar';
import React, {useEffect, useState} from 'react';
import { StyleSheet, Text, View, Alert, Button  } from 'react-native';


import {initNfc, readNdef} from './nfc';
import NfcManager, { NfcTech, TagEvent } from 'react-native-nfc-manager';

export default function App() {
  const [nfcTag, setNfcTag] = useState<TagEvent | null>(null);

  useEffect(() => {
    initNfc().then(() => {});
  }, []);

  // const handleReadNfc = async () => {
  //   try {
  //     const tag = await readNdef();
  //     if (tag) {
  //       setNfcTag(tag);
  //       Alert.alert('Tag lida com sucesso!', JSON.stringify(tag));
  //     } else {
  //       Alert.alert('Nenhuma tag encontrada!');
  //     }
  //   } catch (error) {
  //     console.error('Erro ao ler NFC:', error);
  //     Alert.alert('Erro ao ler NFC', 'Ocorreu um erro ao tentar ler a tag.');
  //   }
  // };

  return (
    <View style={styles.container}>
      <Text style={styles.text}>APROXIME O CARTÃO AO SENSOR</Text>
      {/* <Button title="Ler Tag NFC" onPress={handleReadNfc} />
      {nfcTag && (
        <Text style={styles.tagText}>
          NFC Tag: {JSON.stringify(nfcTag)}
        </Text>
      )} */}
      <StatusBar style="light" backgroundColor="#33cc95" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#33cc95', // Fundo verde
    alignItems: 'center',
    justifyContent: 'center',
  },
  text: {
    fontSize: 48, // Tamanho grande do texto
    fontWeight: 'bold',
    color: '#fff', // Texto em branco para contraste com o fundo
    textAlign: 'center',
    margin: 20,
  },
  tagText: {
    marginTop: 20,
    fontSize: 16,
    color: '#fff',
  },
});
