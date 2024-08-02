import java.lang.instrument.Instrumentation;
import java.lang.instrument.ClassFileTransformer;
import java.security.ProtectionDomain;
import javassist.ClassPool;
import javassist.CtClass;
import javassist.CtMethod;

public class MethodCallLogger {
    public static void premain(String agentArgs, Instrumentation inst) {
        inst.addTransformer(new ClassFileTransformer() {
            @Override
            public byte[] transform(ClassLoader loader, String className, Class<?> classBeingRedefined,
                                    ProtectionDomain protectionDomain, byte[] classfileBuffer) {
                if (className == null || !className.startsWith("org/argouml/") &&
                        !className.startsWith("org/jhotdraw/") &&
                        !className.startsWith("org/jedit/")) {
                    return classfileBuffer;
                }

                try {
                    ClassPool classPool = ClassPool.getDefault();
                    CtClass ctClass = classPool.get(className.replace('/', '.'));
                    for (CtMethod method : ctClass.getDeclaredMethods()) {
                        method.insertBefore("{ System.out.println(\"" + className + "." + method.getName() + "\"); }");
                    }
                    return ctClass.toBytecode();
                } catch (Exception e) {
                    e.printStackTrace();
                }
                return classfileBuffer;
            }
        });
    }
}
