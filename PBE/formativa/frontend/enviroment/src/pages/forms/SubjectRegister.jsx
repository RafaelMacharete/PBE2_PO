// import styles from './TeacherLogin.module.css'
import styles from './principal.module.css'

import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';

const loginSchema = z.object({
    name: z.string().min(3, { message: 'Insert a valid name' }),
    course: z.string().min(2, { message: 'Insert a valid course' }),
    workload: z.string().min(2,{ message: 'Insert a valid workload'}),
    description: z.string().min(1, { message: 'Insert some description' }),
    teacher: z.string().min(3, { message: 'Insert a valid teacher' }),
})

export function SubjectRegister() {
    const { register, handleSubmit, formState: { errors } } = useForm({
        resolver: zodResolver(loginSchema)
    })

    function userAutenticate(data) {
        console.log(data)
    }

    return (
        <div className={styles.container}>
            <p className={styles.title}>Subject Register</p>

            <form
                onSubmit={handleSubmit(userAutenticate)}
                className={styles.form}
            >
                <input
                    {...register('name')}
                    placeholder='name'
                    className={styles.field}
                />
                {errors.name && (<p>{errors.name.message}</p>)}
                <input
                    {...register('course')}
                    placeholder='course'
                    className={styles.field}
                />
                {errors.course && (<p>{errors.course.message}</p>)}
                <input
                    {...register('workload')}
                    placeholder='Workload'
                    className={styles.field}
                />
                {errors.workload && (<p>{errors.workload.message}</p>)}
                <input
                    {...register('description')}
                    placeholder='Description'
                    className={styles.field}
                />
                {errors.description && (<p>{errors.description.message}</p>)}
                <input
                    {...register('teacher')}
                    placeholder='Teacher'
                    className={styles.field}
                />
                {errors.teacher && (<p>{errors.teacher.message}</p>)}
                <button
                    type='submit'
                    className={styles.button}
                >Login</button>
            </form>
        </div>
    );
}
