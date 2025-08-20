# Django-Rest-Framework

### Core principles of REST :

- Stateless : Don't store any information about the client between the request cycles.

- Client-Server architecture

- Standerdized interface : REST API's rely on a set of standard methods (GET, POST, PUT, DELETE) for interacting with resources.

- Easy to read the data.

### Serialization : 

- It's the process of converting the model object or query set into JSON format or any other formats that the client requires.

- Serializers = Translators for your data

- Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. 

- Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

### Types of Serialization : 

**Manual Serialization :** Converting the query set into List.

**Serializers** : Inbuilt functionality

### Deserialization : 

- It's the reverse of serialization.

- The data received from the client, usually in JSON format is converted back into the model instance or a query set.